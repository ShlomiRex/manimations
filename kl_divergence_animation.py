from manim import *
from scipy.stats import norm

class KLDivergence(Scene):
    def construct(self):
        # Title
        title = Tex("KL Divergence: $D_{KL}(P || Q)$").scale(1.2)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": GREY},
            tips=False,
            # use y_length (not height) for vertical size in this Manim version
            y_length=4,
        )
        # place axes below the title so the title doesn't get overlapped
        axes.next_to(title, DOWN, buff=0.7)
        labels = axes.get_axis_labels("x", "p(x)")
        self.play(Create(axes), Write(labels))

        # Define distributions
        p_func = lambda x: norm.pdf(x, 0, 1)
        q_func = lambda x: norm.pdf(x, 1, 1.2)

        # Create plots
        p_graph = axes.plot(p_func, color=BLUE)
        q_graph = axes.plot(q_func, color=RED)

        # Labels
        p_label = MathTex("P(x)").next_to(axes.c2p(-1, 0.4), UP).set_color(BLUE)
        q_label = MathTex("Q(x)").next_to(axes.c2p(1.8, 0.3), UP).set_color(RED)

        # Animate appearance
        self.play(Create(p_graph), Write(p_label))
        self.play(Create(q_graph), Write(q_label))

        # Highlight KL area
        kl_area = axes.get_area(
            p_graph, x_range=[-4, 4], bounded_graph=q_graph,
            color=YELLOW, opacity=0.3
        )
        kl_text = Tex("$D_{KL}(P||Q)$ measures this difference").next_to(axes, DOWN)
        self.play(FadeIn(kl_area))
        self.play(Write(kl_text))

        # Animate small difference
        self.play(
            p_graph.animate.shift(RIGHT * 0.5),
            q_graph.animate.shift(LEFT * 0.5),
            run_time=2
        )

        # After shifting the graphs, compute the new KL area (different color)
        new_kl_area = axes.get_area(
            p_graph, x_range=[-4, 4], bounded_graph=q_graph,
            color=GREEN, opacity=0.4
        )
        # Keep the original area visible and show the new one so the difference is clear.
        # Dim the original slightly for contrast and fade in the new area on top.
        self.play(
            kl_area.animate.set_opacity(0.2),
            FadeIn(new_kl_area),
            run_time=1.5,
        )
        # Keep both areas in the scene for comparison

        self.wait(2)
