"""
control_surfaces

Contains definitions for basic control surface types, which can be extended by
controllers if necessary.

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    # Base types
    'ControlSurface',
    'IControlShadow',
    'ControlShadow',
    'NullControlShadow',
    'ControlShadowList',
    # Control mappings
    'IControlHash',
    'ControlMapping',
    'ControlEvent',
    'ControlShadowEvent',
    # Other imports
    'value_strategies',
    'event_patterns',
    'matchers',
    'managers',
    # Control surfaces
    'NullControl',
    'Note',
    'ModWheel',
    'PitchWheel',
    'StandardModWheel',
    'StandardPitchWheel',
    'Data2PitchWheel',
    'AfterTouch',
    'ChannelAfterTouch',
    'NoteAfterTouch',
    'Pedal',
    'SustainPedal',
    'SostenutoPedal',
    'SoftPedal',
    'Button',
    'TransportButton',
    'PlayButton',
    'StopButton',
    'LoopButton',
    'RecordButton',
    'FastForwardButton',
    'RewindButton',
    'MetronomeButton',
    'NavigationControl',
    'NavigationButton',
    'DpadButtons',
    'DirectionUp',
    'DirectionDown',
    'DirectionLeft',
    'DirectionRight',
    'DirectionSelect',
    'NextPrevButton',
    'DirectionNext',
    'DirectionPrevious',
    'JogWheel',
    'StandardJogWheel',
    'ShiftedJogWheel',
    'MoveJogWheel',
    'GenericFader',
    'Fader',
    'MasterFader',
    'FaderButton',
    'GenericFaderButton',
    'MasterGenericFaderButton',
    'MuteButton',
    'MasterMuteButton',
    'SoloButton',
    'MasterSoloButton',
    'ArmButton',
    'MasterArmButton',
    'SelectButton',
    'MasterSelectButton',
    'GenericKnob',
    'Knob',
    'MasterKnob',
    'Encoder',
    'ModXY',
    'ModX',
    'ModY',
    'DrumPad',
    'ToolSelector',
    'MacroButton',
    'SaveButton',
    'UndoRedoButton',
    'UndoButton',
    'RedoButton',
    'QuantizeButton',
    'CaptureMidiButton',
    'SwitchActiveButton',
    'SwitchActivePluginButton',
    'SwitchActiveWindowButton',
    'SwitchActiveToggleButton',
    'PauseActiveButton',
    'ControlSwitchButton',
    'HintMsg',
    'NotifMsg',
    'Ambient',
]

from .controls import (
    ControlSurface,
    NullControl,
    Note,
    ModWheel,
    PitchWheel,
    StandardModWheel,
    StandardPitchWheel,
    Data2PitchWheel,
    AfterTouch,
    ChannelAfterTouch,
    NoteAfterTouch,
    Pedal,
    SustainPedal,
    SostenutoPedal,
    SoftPedal,
    Button,
    ControlSwitchButton,
    TransportButton,
    PlayButton,
    StopButton,
    LoopButton,
    RecordButton,
    FastForwardButton,
    RewindButton,
    MetronomeButton,
    NavigationControl,
    NavigationButton,
    DpadButtons,
    DirectionUp,
    DirectionDown,
    DirectionLeft,
    DirectionRight,
    DirectionSelect,
    NextPrevButton,
    DirectionNext,
    DirectionPrevious,
    JogWheel,
    StandardJogWheel,
    ShiftedJogWheel,
    MoveJogWheel,
    GenericFader,
    Fader,
    MasterFader,
    FaderButton,
    GenericFaderButton,
    MasterGenericFaderButton,
    MuteButton,
    MasterMuteButton,
    SoloButton,
    MasterSoloButton,
    ArmButton,
    MasterArmButton,
    SelectButton,
    MasterSelectButton,
    GenericKnob,
    Knob,
    MasterKnob,
    Encoder,
    ModXY,
    ModX,
    ModY,
    DrumPad,
    ToolSelector,
    MacroButton,
    SaveButton,
    UndoRedoButton,
    UndoButton,
    RedoButton,
    QuantizeButton,
    CaptureMidiButton,
    SwitchActiveButton,
    SwitchActivePluginButton,
    SwitchActiveWindowButton,
    SwitchActiveToggleButton,
    PauseActiveButton,
    HintMsg,
    NotifMsg,
    Ambient,
)

from .control_shadow import (
    IControlShadow,
    ControlShadow,
    NullControlShadow,
    ControlShadowList,
)
from .control_mapping import (
    IControlHash,
    ControlMapping,
    ControlEvent,
    ControlShadowEvent
)

from . import value_strategies
from . import event_patterns
from . import managers
from . import matchers
