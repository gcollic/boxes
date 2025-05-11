"""Generator for a QMK info.json keyboard."""

from boxes import Boxes, restore

from .keyboard import Keyboard


class QmkKeyboard(Boxes, Keyboard):
    """Generator for a QMK info.json keyboard."""
    ui_group = 'Misc'
    border = 6

    def __init__(self) -> None:
        super().__init__()
        self.add_common_keyboard_parameters()
        self.keys = [
            (0,0.3,0),
            (1,0.3,0),
            (2,0.1,0),
            (3,0,0),
            (4,0.1,0),
            (5,0.2,0),
            (9,0.2,0),
            (10,0.1,0),
            (11,0,0),
            (12,0.1,0),
            (13,0.3,0),
            (14,0.3,0),
            (0,1.3,0),
            (1,1.3,0),
            (2,1.1,0),
            (3,1,0),
            (4,1.1,0),
            (5,1.2,0),
            (9,1.2,0),
            (10,1.1,0),
            (11,1,0),
            (12,1.1,0),
            (13,1.3,0),
            (14,1.3,0),
            (0,2.3,0),
            (1,2.3,0),
            (2,2.1,0),
            (3,2,0),
            (4,2.1,0),
            (5,2.2,0),
            (9,2.2,0),
            (10,2.1,0),
            (11,2,0),
            (12,2.1,0),
            (13,2.3,0),
            (14,2.3,0),
            (0,3.3,0),
            (1,3.3,0),
            (2,3.1,0),
            (3,3,0),
            (4,3.1,0),
            (5,3.2,0),
            (6,3.6,0),
            (8,3.6,0),
            (9,3.2,0),
            (10,3.1,0),
            (11,3,0),
            (12,3.1,0),
            (13,3.3,0),
            (14,3.3,0),
            (0.125,4.3,0),
            (1.375,4.3,0),
            (3.75,4.1,0),
            (5,4.2,15),
            (6.2,4.6,30),
            (7.9339746,5.1,-30),
            (9.034074174,4.458819045,-15),
            (10.25,4.1,0)
        ]

    def render(self):
        """Renders the keyboard."""

        self.moveTo(10, 30)
        case_x, case_y = self._case_x_y()

        margin = 2 * self.border + 1

        # keyholder
        self.outer()
        self.half()
        self.holes()
        self.moveTo(case_x + margin)

        # support
        self.outer()
        self.half(self.support)
        self.holes()
        self.moveTo(-case_x - margin, case_y + margin)

        # hotplug
        self.outer()
        self.half(self.hotplug)
        self.holes()
        self.moveTo(case_x + margin)

        # border
        self.outer()
        self.rim()
        self.holes()
        self.moveTo(-case_x - margin, case_y + margin)

    def holes(self, diameter=3, margin=1.5):
        case_x, case_y = self._case_x_y()
        for x in [-margin, case_x + margin]:
            for y in [-margin, case_y + margin]:
                self.hole(x, y, d=diameter)

    @restore
    def rim(self):
        x, y = self._case_x_y()
        self.moveTo(x * .5, y * .5)
        self.rectangularHole(0, 0, x, y, 5)

    @restore
    def outer(self):
        x, y = self._case_x_y()
        b = self.border
        self.moveTo(0, -b)
        corner = [90, b]
        self.polyline(*([x, corner, y, corner] * 2))

    @restore
    def half(self, hole_cb=None):
        half_btn = Keyboard.SWITCH_CASE_SIZE / 2
        self.moveTo(half_btn, half_btn)
        if hole_cb is None:
            hole_cb = self.key
        self.apply_callback_on_keys(
            hole_cb,
            self.keys
        )

    def support(self):
        self.configured_plate_cutout(support=True)

    def hotplug(self):
        self.pcb_holes(
            with_hotswap=self.hotswap_enable,
            with_pcb_mount=self.pcb_mount_enable,
            with_diode=self.diode_enable,
            with_led=self.led_enable,
        )

    def key(self):
        self.configured_plate_cutout()

    # get case sizes
    def _case_x_y(self):
        spacing = Keyboard.STANDARD_KEY_SPACING
        margin = spacing - self.Keyboard.SWITCH_CASE_SIZE
        max_x = max(x+1 for (x, _, _) in self.keys) * spacing - margin
        max_y = max(y+1 for (_, y, _) in self.keys) * spacing - margin
        return max_x, max_y
