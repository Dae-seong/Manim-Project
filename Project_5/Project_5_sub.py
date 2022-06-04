from manim import *

class Project_5_sub (Scene) :

    def construct (self) :

        self.camera.background_color = WHITE
        Text.set_default (color = BLACK)
        MathTex.set_default (color = BLACK)

        Text_1 = MathTex ("< \\pi <").to_edge (DOWN)
        Text_2 = MathTex ("N = ").to_edge (UL).shift (RIGHT, DOWN * 0.5).scale (1)
        Text_3 = Text ("속도").scale (0.8)
        Text_4 = MathTex ("UP").next_to (Text_3, RIGHT * 1.5)

        VGroup (Text_3, Text_4).move_to ([0, 0.7, 0])

        s = 0.6
        w = 3
        min = 5
        max = 100
        r = 2.5
        
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

        circle = Circle (radius = 2.5).set_color (BLACK).shift (UP * 0.7)

        for n in range (min, max + 1) :

            out_dot [n] = [0] * (n + 1)
            out_line [n] = [0] * (n + 1)
            in_dot [n] = [0] * (n + 1)
            in_line [n] = [0] * (n + 1)

            for k in range (1, n + 1) :

                out_dot [n] [k] = Dot ([(np.sin (2*PI * k/n) * r) / np.cos (PI/n), (np.cos (2*PI * k/n) * r) / np.cos (PI/n), 0], radius = 0).shift (UP * 0.7).get_center ()
                in_dot [n] [k] = Dot ([np.sin (2*PI * k/n) * r, np.cos (2*PI * k/n) * r, 0], radius = 0).shift (UP * 0.7).get_center ()

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

        def func (x, y) :

            self.play (
                vt_1.animate.set_value (x * np.tan (PI / x)),
                vt_2.animate.set_value (x * np.sin (PI / x)),
                vt_3.animate.set_value (x),
                ReplacementTransform (out_line [x - y], out_line [x]),
                ReplacementTransform (in_line [x - y], in_line [x]),
                )

        self.play (FadeIn (circle))
        self.wait (1)

        self.play (FadeIn (VGroup (out_line [min], in_line [min], Text_2, vertex)))
        self.wait (1)

        self.play (FadeIn (VGroup (Text_1, out_number, in_number)))
        self.wait (1)

        for n in range (min + 1, max + 1) :

            if (n <= 10) :

                func (n, 1)

                self.wait (1)

                if (n == 10) :

                    self.play (FadeIn (Text_3, Text_4))
                    self.wait (0.1)

                    self.play (FadeOut (Text_3, Text_4))
                    self.wait (0.7)

            if ((n % 10) == 0) and (n >= 20) and (n <= 50) :

                func (n, 10)

                self.wait (0.5)

        self.play (FadeOut (VGroup (circle, out_line [50], in_line [50])))

        self.play (VGroup (Text_1, out_number, in_number).animate.move_to (ORIGIN))
        self.wait (1)

        for n in range (3, 5 + 1) :

            self.play (
                vt_1.animate.set_value ((10 ** n) * np.tan (PI / (10 ** n))),
                vt_2.animate.set_value ((10 ** n) * np.sin (PI / (10 ** n))),
                vt_3.animate.set_value ((10 ** n))
                )

            self.wait (1.5)