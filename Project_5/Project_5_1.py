from manim import *

class Introduction_pi_1 (Scene) :

    def construct(self):

        self.camera.background_color = WHITE
        Text.set_default (color = BLACK)
        Line.set_default (color = BLACK)
        VMobject.set_default (color = BLACK)
        
        s = 0.8

        Text_1 = Text ("원의 중심").shift (UP * 2.75).scale (s)
        Text_2 = Text ("반지름").move_to (Text_1).scale (s)
        Text_3 = Text ("원").move_to (Text_1).scale (s)
        Text_4 = Text ("지름").move_to (Text_1).scale (s).set_color ("#FF0000")
        Text_5 = Text ("원주").move_to (Text_1).scale (s).set_color ("#FF0000")
        Text_6 = Text ("÷").move_to (Text_1).scale (s)
        Text_7 = Text ("=").move_to ([0, -2, 0]).scale (0.9)
        Text_7_copy = Text_7.copy ()
        Text_8 = Text ("원주율").scale (s).move_to ([0, 0.4, 0])
        Text_9 = MathTex ("0{{.141592 \\cdots}}").next_to (Text_7, RIGHT)
        Text_10 = MathTex ("\\pi").move_to ([0, 0.3, 0])

        dot_1 = Dot ([0, 0.5, 0], radius = 0.03).set_color (BLACK)
        dot_2 = Dot ([1.5, 0.5, 0], radius = 0.03).set_color (BLACK)

        line_1 = Line (dot_1.get_center (), dot_2.get_center ()).set_stroke (width = 5.5)
        line_2 = VMobject ().set_stroke (width = 5.5)
        line_2.set_points_as_corners ([dot_1.get_center (), dot_1.get_center ()])
        line_3 = VMobject ().set_stroke (width = 5.5)
        line_4 = VMobject ().set_stroke (width = 5.5)
        line_5 = Line ([-1.5*PI, 0, 0], [1.5*PI, 0, 0]).set_stroke (width = 5.5).set_color ("#FF0000")
        line_6 = Line ([-1.5*PI + 9, 0, 0], [1.5*PI, 0, 0]).set_color ("#FF0000").set_stroke (width = 5.5)
        line_7 = VMobject ().set_color ("#FF0000").set_stroke (width = 5.5)

        radius = VGroup (line_1, dot_2)

        circle_1 = VMobject ().set_stroke (width = 5.5)
        circle_1.set_points_as_corners ([dot_2.get_center (), dot_2.get_center ()])
        circle_2 = Circle (radius = 1.5).set_color (BLACK).set_stroke (width = 5.5).move_to ([0, 0.5, 0])

        number = DecimalNumber (1, num_decimal_places = 0).set_color (BLACK)

        vt_1 = ValueTracker (1)

        def rotate_radius (mob, dt) :

            mob.rotate (dt * 3, about_point = [0, 0.5, 0])

        def draw_circle (mob) :

            prev = mob.copy ()
            prev.add_points_as_corners ([dot_2.get_center ()])
            mob.become (prev)

        def move_dot_left (mob, dt) :

            mob.shift (LEFT * dt * 2)
        
        def move_dot_right (mob, dt) :

            mob.shift (RIGHT * dt * 2)

        def draw_radius (mob) :

            prev = mob.copy ()
            prev.add_points_as_corners ([dot_1.get_center ()])
            mob.become (prev)

        def draw_line (mob) :

            prev = mob.copy ()
            prev.add_points_as_corners ([dot_2.get_center ()])
            mob.become (prev)

        def move_number (mob) :
            
            mob.next_to (brace, DOWN)

        self.play (FadeIn (dot_1))
        self.wait (1)

        self.play (FadeIn (Text_1))
        self.wait (1)

        self.play (FadeOut (Text_1))
        self.wait (0.5)

        self.play (FadeIn (dot_2))
        self.wait (0.5)

        self.play (Write (line_1))
        self.wait (1)

        self.play (FadeIn (Text_2))
        self.wait (1)

        self.play (FadeOut (Text_2))
        self.wait (1)

        radius.add_updater (rotate_radius)
        circle_1.add_updater (draw_circle)

        self.add (radius, circle_1)
        self.wait (PI * 2/3)

        radius.remove_updater (rotate_radius)
        circle_1.remove_updater (draw_circle)
        self.add (circle_2)
        self.wait (1)

        self.play (FadeIn (Text_3))
        self.wait (1)

        self.play (FadeOut (Text_3))
        self.wait (1)

        dot_1.add_updater (move_dot_left)
        line_2.add_updater (draw_radius)

        self.add (line_2)
        self.wait (0.75)

        dot_1.remove_updater (move_dot_left)
        line_2.remove_updater (draw_radius)

        self.wait (1)

        self.play (FadeIn (Text_4), VGroup (line_1, line_2, dot_1, dot_2).animate.set_color ("#FF0000"))
        self.wait (1)

        self.play (FadeOut (Text_4),  VGroup (line_1, line_2, dot_1, dot_2).animate.set_color (BLACK))
        self.wait (1)

        diameter = VGroup (line_1, line_2, dot_1, dot_2)

        self.play (diameter.animate.move_to ([-1.5*PI + 1.5, -2, 0]))
        self.wait (1)

        self.play (FadeIn (Text_5), circle_2.animate.set_color ("#FF0000"))
        self.wait (1)

        self.play (FadeOut (circle_2), FadeIn (line_5))
        self.wait (1)

        self.play (FadeOut (Text_5), line_5.animate.set_color (BLACK))
        self.wait (1)

        Text_5.next_to (Text_6, LEFT).set_color (BLACK)
        Text_4.next_to (Text_6, RIGHT).set_color (BLACK)

        self.play (FadeIn (VGroup (Text_4, Text_5, Text_6)))
        self.wait (1)

        brace = always_redraw (lambda : BraceBetweenPoints (dot_1.get_center (), dot_2.get_center ()).set_color (BLACK))

        number.next_to (brace, DOWN)

        number.add_updater (lambda mob : mob.set_value (vt_1.get_value ()))
        number.add_updater (move_number)

        line_3.set_points_as_corners ([dot_2.get_center (), dot_2.get_center ()])
        line_4.set_points_as_corners ([dot_2.get_center (), dot_2.get_center ()])        

        self.play (FadeIn (VGroup (brace, number)))
        self.wait (1)

        self.add (line_3)

        dot_2.add_updater (move_dot_right)
        line_3.add_updater (draw_line)

        self.play (vt_1.animate.set_value (2), run_time = 1.5)

        dot_2.remove_updater (move_dot_right)
        line_3.remove_updater (draw_line)

        self.wait (1)

        line_4.move_to (dot_2)

        self.add (line_4)

        dot_2.add_updater (move_dot_right)
        line_4.add_updater (draw_line)

        self.play (vt_1.animate.set_value (3), run_time = 1.5)

        dot_2.remove_updater (move_dot_right)
        line_4.remove_updater (draw_line)
        number.remove_updater (move_number)

        self.wait (1)

        self.play (VGroup (diameter, line_4).animate.set_color (WHITE))
        self.wait (1)

        long_line = VGroup (line_1, line_2, line_3, line_4, brace, number, dot_1, dot_2)

        self.play (long_line.animate.shift (UP * 2))
        self.remove (dot_2)
        self.wait (1)

        self.play (FadeIn (line_6))
        self.wait (1)

        self.play (line_6.animate.next_to (Text_7, LEFT))
        self.play (FadeIn (Text_7))
        self.wait (1)

        self.play (FadeIn (Text_9))
        self.wait (1)

        self.play (FadeIn (dot_2.set_color ("#FF0000")))

        line_7.set_points_as_corners ([dot_2.get_center (), dot_2.get_center ()])

        self.add (line_7)

        dot_2.add_updater (move_dot_right)
        line_7.add_updater (draw_line)
        #number.add_updater (move_number)

        self.play (vt_1.animate.set_value (3), run_time = 3 * (PI - 3) / 2)

        dot_2.remove_updater (move_dot_right)
        line_7.remove_updater (draw_line)

        self.wait (0.5)

        self.play (
            Text_9.submobjects [1].animate.next_to (number, RIGHT * 0.45),
            FadeOut (VGroup (line_6, Text_7, Text_9.submobjects [0]))
            )
        self.wait (1)

        self.play (
            FadeOut (line_1),
            FadeOut (line_2),
            FadeOut (line_3),
            FadeOut (line_4),
            FadeOut (line_5),
            FadeOut (line_7),
            FadeOut (dot_1),
            FadeOut (dot_2),
            FadeOut (brace)
            )
        self.wait (1)

        Pi = VGroup (number, Text_9.submobjects [1])

        self.play (
            Pi.animate.move_to ([0.5, -0.4, 0]),
            VGroup (Text_4, Text_5, Text_6).animate.move_to ([0, 0.4, 0]),
            FadeIn (Text_7_copy.move_to ([-1.15, -0.4, 0]))
            )
        self.wait (1)

        self.play (FadeOut (VGroup (Text_4, Text_5, Text_6)))
        self.wait (0.5)
        
        self.play (FadeIn (Text_8))
        self.wait (1)

        self.play (FadeOut (Text_8))
        self.wait (0.5)

        self.play (FadeIn (Text_10))
        self.wait (1)

        self.play (FadeOut (Pi, Text_7_copy, Text_10))
        self.wait (1)