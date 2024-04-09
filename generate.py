import cairo

from conversions import *

QX = 1.041767903257093
BX = -0.03742242410656686
QY = 1.0402216402768423
BY = -0.17030778441270802

A4_W_INCH = 8.3
A4_H_INCH = 11.7


def x2real(value: float) -> float:
    """Applies correction to the given dimension in x direction."""
    return QX * value + BX


def y2real(value: float) -> float:
    """Applies correction to the given dimension in y direction."""
    return QY * value + BY


def generate(
    output_name: str,
    image_name: str,
    img_w_mm: float,
    img_h_mm: float,
    border_w_mm: float | None,
    border_h_mm: float | None,
) -> None:
    """Generates PDF with PNG image and optional border in the center of the page."""
    with cairo.PDFSurface(
        output_name, inch2point(A4_W_INCH), inch2point(A4_H_INCH)
    ) as surface:

        ctx = cairo.Context(surface)
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(1)
        ctx.set_font_size(8)
        ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        if not (border_w_mm is None or border_h_mm is None):
            ctx.rectangle(
                (inch2point(A4_W_INCH) - mm2point(x2real(border_w_mm))) / 2,
                (inch2point(A4_H_INCH) - mm2point(y2real(border_h_mm))) / 2,
                mm2point(x2real(border_w_mm)),
                mm2point(y2real(border_h_mm)),
            )
            ctx.stroke()

        image = cairo.ImageSurface.create_from_png(image_name)
        w = image.get_height()
        h = image.get_width()

        ctx.translate(
            (inch2point(A4_W_INCH) - mm2point(x2real(img_w_mm))) / 2,
            (inch2point(A4_H_INCH) - mm2point(y2real(img_h_mm))) / 2,
        )
        ctx.scale(mm2point(x2real(img_w_mm)) / h, mm2point(y2real(img_h_mm)) / w)
        ctx.set_source_surface(image)
        ctx.paint()


if __name__ == "__main__":
    generate("marker_30_50.pdf", "marker.png", 30, 30, 50, 50)
    generate("marker_90_120.pdf", "marker.png", 90, 90, 120, 120)
    generate("marker_130.pdf", "marker.png", 130, 130, None, None)
