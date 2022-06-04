from msilib.schema import Font
from tkinter import font
from manim import *

class Introduction_pi_2 (Scene) :

    def construct (self) :

        self.camera.background_color = WHITE
        Text.set_default (color = BLACK)
        VMobject.set_default (color = BLACK)

        Text_1 = MathTex ("< \\pi <").set_color (BLACK).to_edge (DOWN)
        Text_2 = MathTex ("N = ").set_color (BLACK).to_edge (UL).shift (RIGHT, DOWN * 0.5).scale (1)

        s = 0.6
        w = 3
        min = 5
        max = 100
        
        vt_1 = ValueTracker (min * np.tan (PI/min))
        vt_2 = ValueTracker (min * np.sin (PI/min))
        vt_3 = ValueTracker (min)

        out_line = [0] * (max + 1)
        out_dot = [0] * (max + 1)
        out_color = "#2DAC44"

        out_number = DecimalNumber (num_decimal_places = 10).set_color (out_color)
        out_number.add_updater (lambda x : x.set_value (vt_1.get_value ())).next_to (Text_1, RIGHT)

        in_line = [0] * (max + 1)
        in_dot = [0] * (max + 1)
        in_color = YELLOW_E

        in_number = DecimalNumber (num_decimal_places = 10).set_color (in_color)
        in_number.add_updater (lambda x : x.set_value (vt_2.get_value ())).next_to (Text_1, LEFT)

        vertex = DecimalNumber (num_decimal_places = 0).scale (1)
        vertex.add_updater (lambda x : x.set_value (vt_3.get_value ())).set_color (BLACK).next_to (Text_2, RIGHT * 1).shift (DOWN * 0.03)

        circle_1 = Circle (radius = 1.3).set_color (BLACK).move_to ([4, 0, 0])
        circle_2 = Circle (radius = 2.5).set_color (BLACK).shift (UP * 0.7)

        def polygon (r, x, y, min, max) :

            for n in range (min, max + 1) :

                out_dot [n] = [0] * (n + 1)
                out_line [n] = [0] * (n + 1)
                in_dot [n] = [0] * (n + 1)
                in_line [n] = [0] * (n + 1)

                for k in range (1, n + 1) :

                    out_dot [n] [k] = Dot ([(np.sin (2*PI * k/n) * r) / np.cos (PI/n), (np.cos (2*PI * k/n) * r) / np.cos (PI/n), 0], radius = 0).shift (RIGHT * x, UP * y).get_center ()
                    in_dot [n] [k] = Dot ([np.sin (2*PI * k/n) * r, np.cos (2*PI * k/n) * r, 0], radius = 0).shift (RIGHT * x, UP * y).get_center ()

                for k in range (1, n + 1) :

                    if (k == n) :

                        in_line [n] [k] = Line (in_dot [n] [k], in_dot [n] [1]).set_stroke (width = w)
                        out_line [n] [k] = Line (out_dot [n] [k], out_dot [n] [1]).set_stroke (width = w)

                        break
                        
                    out_line [n] [k] = Line (out_dot [n] [k], out_dot [n] [k + 1]).set_stroke (width = w)
                    in_line [n] [k] = Line (in_dot [n] [k], in_dot [n] [k + 1]).set_stroke (width = w)

                out_line [n].pop (0)
                in_line [n].pop (0)

                out_line [n] = VGroup (*[out_line [n] [i] for i in range (0, n)]).set_color (out_color)
                in_line [n] = VGroup (*[in_line [n] [i] for i in range (0, n)]).set_color (in_color)

        def func_1 (x, y) :

            self.play (
                ReplacementTransform (out_line [x - y], out_line [x]),
                ReplacementTransform (in_line [x - y], in_line [x]),
                )

        def func_2 (x, y) :

            self.play (
                vt_1.animate.set_value (x * np.tan (PI / x)),
                vt_2.animate.set_value (x * np.sin (PI / x)),
                vt_3.animate.set_value (x),
                ReplacementTransform (out_line [x - y], out_line [x]),
                ReplacementTransform (in_line [x - y], in_line [x]),
                )

        Text_4 = Text ("원주율의 소수점 뒷자리는 끝없이 이어진다.").scale (s)
        Text_4_1 = MathTex ("\\pi = 3.1415926535897932384626433832795028\\\\841971693993751097494459230781640628 \\cdots").scale (0.7).next_to (Text_4, DOWN * 2)
        Text_5 = Text ("이와 같은 수를 무리수라고 한다.").scale (s).next_to (Text_4_1, DOWN * 2)
        Text_6 = Text ("원주율의 근삿값은 다양한 방법으로 구할 수 있다.").scale (s)
        Text_7 = Text ("저명한 수학자인 아르키메데스는").scale (s).next_to (Text_6, DOWN * 2)
        Text_8 = Text ("놀라운 방법으로 원주율의 근삿값을 구하였다.").scale (s).next_to (Text_7, DOWN * 2)
        Text_9 = Text ("방법은 다음과 같다.").scale (s).next_to (Text_8, DOWN * 2)
        Text_10 = Text ("지름이 1인 원을 그린다.").scale (s)
        Text_11 = Text ("원에 외접하는 정다각형과").scale (s).next_to (Text_10, DOWN * 2)
        Text_12 = Text ("원에 내접하는 정다각형을 그린다.").scale (s).next_to (Text_11, DOWN * 2)
        Text_13 = Text ("이제 두 정다각형의 길이를 구한다.").scale (s).next_to (Text_12, DOWN * 2)
        Text_14 = Text ("정다각형의 변의 개수를 늘리면").scale (s)
        Text_15 = Text ("원의 둘레에 근사한다.").scale (s).next_to (Text_14, DOWN * 2)
        Text_16 = Text ("이제 아르키메데스의 방법으로").scale (s).next_to (Text_15, DOWN * 2)
        Text_17 = Text ("원주율의 근삿값을 구해보자.").scale (s).next_to (Text_16, DOWN * 2,)
        Text_18 = Text ("속도").scale (0.8)
        Text_19 = MathTex ("UP").next_to (Text_18, RIGHT * 1.5)
        Text_20 = Text ("원주율은 실생활에서 널리 쓰이고 있다.").scale (s)
        Text_21 = Text ("특히 수학과 과학에서 어떤 상수와 함께 엄청 중요한 상수로 여겨진다.").scale (s).next_to (Text_20, DOWN * 2)
        Text_22 = MathTex ("End").scale (2.5)

        VGroup (Text_4, Text_4_1, Text_5).move_to (ORIGIN)
        VGroup (Text_6, Text_7, Text_8, Text_9).move_to (ORIGIN)
        VGroup (Text_10, Text_11, Text_12, Text_13).move_to ([-2, 0, 0])
        VGroup (Text_14, Text_15, Text_16, Text_17).move_to ([-2, 0, 0])
        VGroup (Text_18, Text_19).move_to ([0, 0.7, 0])
        VGroup (Text_20, Text_21).move_to (ORIGIN)
        
        polygon (1.3, 4, 0, min, 10)

        self.play (FadeIn (Text_4))
        self.wait (1)

        self.play (Write (Text_4_1), run_time = 3)
        self.wait (1)

        self.play (FadeIn (Text_5))
        self.wait (1)

        self.play (FadeOut (VGroup (Text_4, Text_4_1, Text_5)))
        self.wait (1.5)

        self.play (FadeIn (Text_6))
        self.wait (1.5)

        self.play (FadeIn (Text_7), FadeIn (Text_8))
        self.wait (2)

        self.play (FadeIn (Text_9))
        self.wait (1)

        self.play (FadeOut (VGroup (Text_6, Text_7, Text_8, Text_9)))
        self.wait (1)

        self.play (FadeIn (Text_10))
        self.wait (1)

        self.play (FadeIn (circle_1))
        self.wait (1)

        self.play (FadeIn (VGroup (Text_11, Text_12)))
        self.wait (2)

        self.play (
            FadeIn (out_line [5]),
            VGroup (*[Text_11.submobjects [i] for i in range (2, 10)]).animate.set_color (out_color)
            )
        self.wait (1)

        self.play (
            FadeIn (in_line [5]),
            VGroup (*[Text_12.submobjects [i] for i in range (2, 10)]).animate.set_color (in_color)
            )
        self.wait (1)

        self.play (FadeIn (Text_13))
        self.wait (1)

        self.play (FadeOut (VGroup (Text_10, Text_11, Text_12, Text_13)))
        self.wait (1)

        self.play (FadeIn (Text_14, Text_15))
        self.wait (1)

        for i in range (6, 8 + 1) :

            func_1 (i, 1)

            self.wait (1)

        self.play (FadeIn (VGroup (Text_16, Text_17)))
        self.wait (2)

        self.play (FadeOut (VGroup (Text_14, Text_15, Text_16, Text_17, circle_1, out_line [8], in_line [8])))
        self.wait (1)

        polygon (2.5, 0, 0.7, min, max)

        self.play (FadeIn (circle_2))
        self.wait (1)

        self.play (FadeIn (VGroup (out_line [min], in_line [min], Text_2, vertex)))
        self.wait (1)

        self.play (FadeIn (VGroup (Text_1, out_number, in_number)))
        self.wait (1)

        for n in range (min + 1, max + 1) :

            if (n <= 10) :

                func_2 (n, 1)

                self.wait (1.5)

                if (n == 10) :

                    self.play (FadeIn (Text_18, Text_19))
                    self.wait (1)

                    self.play (FadeOut (Text_18, Text_19))
                    self.wait (1)

            if ((n % 10) == 0) and (n >= 20) and (n <= 50) :

                func_2 (n, 10)

                self.wait (0.5)

        self.play (FadeOut (VGroup (circle_2, out_line [50], in_line [50])))

        self.play (VGroup (Text_1, out_number, in_number).animate.move_to (ORIGIN))
        self.wait (1)

        for n in range (3, 5 + 1) :

            self.play (
                vt_1.animate.set_value ((10 ** n) * np.tan (PI / (10 ** n))),
                vt_2.animate.set_value ((10 ** n) * np.sin (PI / (10 ** n))),
                vt_3.animate.set_value ((10 ** n))
                )

            self.wait (1.5)

        self.wait (1)

        self.play (FadeOut (VGroup (Text_1, Text_2, out_number, in_number, vertex)))
        self.wait (1)

        self.play (FadeIn (Text_20))
        self.wait (1.5)

        self.play (FadeIn (Text_21))
        self.wait (3)

        self.play (FadeOut (VGroup (Text_20, Text_21)))
        self.wait (1.2)

        self.play (FadeIn (Text_22))
        self.wait (1)