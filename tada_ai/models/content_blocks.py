from typing import Literal, Union
from pydantic import Field

from tada_ai.models.api_model import ApiModel

import csv
from io import StringIO


class Location(ApiModel):
    x0: float
    y0: float
    x1: float
    y1: float
    page_num: int


class BaseContentBlock(ApiModel):
    id: str
    full_word_count: int


class TableCellContentBlock(BaseContentBlock):
    type: Literal["TableCell"] = "TableCell"
    location: Location
    text: str
    rows: tuple[int, ...]
    cols: tuple[int, ...]

    def dfs(self):
        yield self


class TableContentBlock(BaseContentBlock):
    type: Literal["Table"] = "Table"
    locations: list[Location]
    children: list[TableCellContentBlock]

    def to_csv(self):
        col_row_value: dict[tuple[int, int], str] = dict()
        for cell in self.children:
            for col in cell.cols:
                for row in cell.rows:
                    col_row_value[(col, row)] = cell.text

        # Find the dimensions of the table
        max_row = max(max(cell.rows) for cell in self.children)
        max_col = max(max(cell.cols) for cell in self.children)

        csv_file = StringIO()
        writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")

        for row_num in range(max_row + 1):
            row = [
                col_row_value.get((col_num, row_num), "")
                for col_num in range(max_col + 1)
            ]
            writer.writerow(row)

        csv_file.seek(0)
        return csv_file.read()

    def to_markdown(self, first_line_as_header=False) -> str:
        col_row_value: dict[tuple[int, int], str] = dict()
        for cell in self.children:
            for col in cell.cols:
                for row in cell.rows:
                    col_row_value[(col, row)] = cell.text.replace("|", r"\|").replace(
                        "\n", "<br>"
                    )

        max_row = max(max(cell.rows) for cell in self.children)
        max_col = max(max(cell.cols) for cell in self.children)

        rows = []
        start = 0
        if first_line_as_header:
            row = " | ".join(
                col_row_value.get((col_num, 0), "") for col_num in range(max_col + 1)
            )
            rows.append(f"| {row} |")
            row = " | ".join(["-------"] * (max_col + 1))
            rows.append(f"| {row} |")
            start = 1

        for row_num in range(start, max_row + 1):
            row = " | ".join(
                col_row_value.get((col_num, row_num), "")
                for col_num in range(max_col + 1)
            )
            rows.append(f"| {row} |")

        return "\n".join(rows)

    def dfs(self):
        yield self
        yield from self.children


class RootContentBlock(BaseContentBlock):
    type: Literal["Root"] = "Root"
    children: list[
        Union[
            "HeaderContentBlock",
            "ListContentBlock",
            "ParagraphContentBlock",
            "TableContentBlock",
        ]
    ] = Field(discriminator="type")

    def __iter__(self):
        yield from self.dfs()

    def dfs(self):
        """
        A Pre-order depth-first-search implementation.
        This returns all content blocks in the order that they appear in the document
        """
        yield self
        for c in self.children:
            yield from c.dfs()


class HeaderContentBlock(BaseContentBlock):
    type: Literal["Header"] = "Header"
    locations: list[Location]
    text: str
    children: list[
        Union[
            "HeaderContentBlock",
            "ListContentBlock",
            "ParagraphContentBlock",
            "TableContentBlock",
        ]
    ] = Field(discriminator="type")

    def dfs(self):
        yield self
        for c in self.children:
            yield from c.dfs()


class ParagraphContentBlock(BaseContentBlock):
    type: Literal["Paragraph"] = "Paragraph"
    locations: list[Location]
    text: str

    def dfs(self):
        yield self


class ListContentBlock(BaseContentBlock):
    type: Literal["List"] = "List"
    locations: list[Location]
    children: list[Union["ListItemContentBlock", "ListContentBlock"]] = Field(
        discriminator="type"
    )

    def dfs(self):
        yield self
        for c in self.children:
            yield from c.dfs()


class ListItemContentBlock(BaseContentBlock):
    type: Literal["ListItem"] = "ListItem"
    locations: list[Location]
    text: str

    def dfs(self):
        yield self


ContentBlock = (
    HeaderContentBlock
    | ListContentBlock
    | ListItemContentBlock
    | ParagraphContentBlock
    | TableContentBlock
    | TableCellContentBlock
)
