from manimlib import *
import numpy as np

class PythagorasProof(Scene):
    def construct(self):
        # Right triangle with legs a and b
        triangle = Polygon(ORIGIN, RIGHT*3, UP*2, color=WHITE)
        labels = VGroup(
            Text("a").next_to(triangle.get_vertices()[1], DOWN),
            Text("b").next_to(triangle.get_vertices()[2], LEFT),
            Text("c").next_to(triangle.get_vertices()[0]+RIGHT*1.5+UP*1, UR)
        )

        self.play(ShowCreation(triangle, run_time=2))
        self.play(Write(labels, run_time=2))
        self.wait(2)

        # Squares on each side
        square_a = Square(side_length=3, color=BLUE).next_to(triangle, DOWN, buff=0)
        square_b = Square(side_length=2, color=GREEN).next_to(triangle, LEFT, buff=0)
        square_c = Square(side_length=np.hypot(3,2), color=RED).move_to(triangle.get_vertices()[1]+UP*1+RIGHT*1)
        square_c.rotate(-np.arctan(2/3), about_point=triangle.get_vertices()[1])

        self.play(ShowCreation(square_a, run_time=2), ShowCreation(square_b, run_time=2))
        self.wait(2)
        self.play(TransformFromCopy(triangle, square_c, run_time=3))
        self.wait(2)

        # Display equation
        equation = Tex(r"a^2 + b^2 = c^2").to_edge(UP)
        self.play(Write(equation, run_time=2))
        self.wait(4)

        # Rearrangement proof idea
        big_square = Square(side_length=5, color=YELLOW)
        tri1 = triangle.copy().set_fill(BLUE_E, opacity=0.5)
        tri2 = tri1.copy().flip()
        tri3 = tri1.copy().rotate(PI/2)
        tri4 = tri2.copy().rotate(PI/2)
        group = VGroup(tri1, tri2, tri3, tri4).arrange_in_grid(2,2)
        group.move_to(ORIGIN)

        self.play(FadeOut(triangle), FadeOut(square_a), FadeOut(square_b), FadeOut(square_c), FadeOut(labels))
        self.play(Create(big_square, run_time=2))
        self.play(FadeIn(group, run_time=2))
        self.wait(2)
        self.play(FadeOut(group, run_time=2))
        self.wait(4)

        conclusion = Text("Therefore, a^2 + b^2 = c^2").to_edge(DOWN)
        self.play(Write(conclusion, run_time=2))
        self.wait(4)

