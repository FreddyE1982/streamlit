from __future__ import annotations

from typing import TYPE_CHECKING, cast

from streamlit.elements.lib.layout_utils import Width
from streamlit.elements.lib.utils import Key
from streamlit.runtime.metrics_util import gather_metrics
from streamlit.runtime.state import WidgetArgs, WidgetCallback, WidgetKwargs
from streamlit.elements.widgets.button_group import ButtonGroupMixin

if TYPE_CHECKING:
    from streamlit.delta_generator import DeltaGenerator


class RatingMixin(ButtonGroupMixin):
    """Display a star rating widget."""

    @gather_metrics("rating")
    def rating(
        self,
        *,
        key: Key | None = None,
        disabled: bool = False,
        on_change: WidgetCallback | None = None,
        args: WidgetArgs | None = None,
        kwargs: WidgetKwargs | None = None,
        width: Width = "content",
    ) -> int | None:
        return self.feedback(
            "stars",
            key=key,
            disabled=disabled,
            on_change=on_change,
            args=args,
            kwargs=kwargs,
            width=width,
        )

    @property
    def dg(self) -> DeltaGenerator:
        """Get our DeltaGenerator."""
        return cast("DeltaGenerator", self)
