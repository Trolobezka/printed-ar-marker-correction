# type: ignore

import cairo
import numpy as np

from conversions import *

A4_W_INCH = 8.3
A4_H_INCH = 11.7
MARGIN_MM = 15
START_LENGTH_MM = 1
END_LENGTH_MM = 140
LENGTH_COUNT = 40


def generate_calibration_x_pdf() -> None:
    """Generates PDF with calibration lines for x direction."""
    with cairo.PDFSurface(
        "calibration_x.pdf", inch2point(A4_W_INCH), inch2point(A4_H_INCH)
    ) as surface:
        lengths_mm: list[float] = list(
            np.logspace(
                np.log10(START_LENGTH_MM),
                np.log10(END_LENGTH_MM),
                LENGTH_COUNT,
            )
        )
        gap = (inch2point(A4_W_INCH) - 2 * mm2point(MARGIN_MM)) / (LENGTH_COUNT - 1)
        start_width = (
            inch2point(A4_W_INCH) - 2 * mm2point(MARGIN_MM) - mm2point(END_LENGTH_MM)
        ) / 2
        start_height = (
            inch2point(A4_H_INCH) - 2 * mm2point(MARGIN_MM) - (LENGTH_COUNT * gap)
        ) / 2

        print(f"calibration x lengths: {lengths_mm}")

        ctx = cairo.Context(surface)
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(1)
        ctx.set_font_size(8)
        ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        for i, length_mm in enumerate(list(lengths_mm)):
            ctx.move_to(
                start_width + mm2point(MARGIN_MM),
                start_height + mm2point(MARGIN_MM) + i * gap,
            )
            ctx.line_to(
                start_width + mm2point(MARGIN_MM + length_mm),
                start_height + mm2point(MARGIN_MM) + i * gap,
            )
            ctx.stroke()

            ctx.move_to(
                start_width + mm2point(MARGIN_MM + length_mm + 3),
                start_height + mm2point(MARGIN_MM) + i * gap,
            )
            ctx.show_text(f"{length_mm:.3f}")


def generate_calibration_y_pdf() -> None:
    """Generates PDF with calibration lines for y direction."""
    with cairo.PDFSurface(
        "calibration_y.pdf", inch2point(A4_W_INCH), inch2point(A4_H_INCH)
    ) as surface:
        lengths_mm: list[float] = list(
            np.logspace(
                np.log10(START_LENGTH_MM),
                np.log10(END_LENGTH_MM),
                LENGTH_COUNT,
            )
        )
        gap = (inch2point(A4_W_INCH) - 2 * mm2point(MARGIN_MM)) / (LENGTH_COUNT - 1)
        start_width = (
            inch2point(A4_W_INCH) - 2 * mm2point(MARGIN_MM) - (LENGTH_COUNT * gap)
        ) / 2
        start_height = (
            inch2point(A4_H_INCH) - 2 * mm2point(MARGIN_MM) - mm2point(END_LENGTH_MM)
        ) / 2

        print(f"calibration x lengths: {lengths_mm}")

        ctx = cairo.Context(surface)
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(1)
        ctx.set_font_size(8)
        ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        for i, length_mm in enumerate(list(lengths_mm)):
            ctx.move_to(
                start_width + mm2point(MARGIN_MM) + i * gap,
                start_height + mm2point(MARGIN_MM),
            )
            ctx.line_to(
                start_width + mm2point(MARGIN_MM) + i * gap,
                start_height + mm2point(MARGIN_MM + length_mm),
            )
            ctx.stroke()

            ctx.move_to(
                start_width + mm2point(MARGIN_MM) + i * gap,
                start_height + mm2point(MARGIN_MM + length_mm + 3),
            )
            ctx.rotate(np.pi / 2)
            ctx.show_text(f"{length_mm:.3f}")
            ctx.rotate(-np.pi / 2)


if __name__ == "__main__":
    generate_calibration_x_pdf()
    generate_calibration_y_pdf()
