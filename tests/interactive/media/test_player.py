"""
Interactively test the Player in pyglet.media for playing back sounds.
"""
import pytest
from time import sleep

import pyglet
from pyglet.media.player import Player
from pyglet.media.sources import procedural
from pyglet.media.sources.base import StaticSource

#pyglet.options['debug_media'] = True


@pytest.mark.requires_user_validation
def test_play_queue(interactive):
    """Test playing a single sound on the queue."""
    source = procedural.WhiteNoise(1.0)
    player = Player()
    player.play()
    player.queue(source)

    # Pause for the duration of the sound
    sleep(1.0)

    interactive.ask_question('Did you hear white noise for 1 second?')

@pytest.mark.requires_user_validation
def test_queue_play(interactive):
    """Test putting a single sound on the queue and then starting the player."""
    source = procedural.WhiteNoise(1.0)
    player = Player()
    player.queue(source)
    player.play()

    # Pause for the duration of the sound
    sleep(1.0)

    interactive.ask_question('Did you hear white noise for 1 second?')

@pytest.mark.requires_user_validation
def test_pause_queue(interactive):
    """Test the queue is not played when player is paused."""
    source = procedural.WhiteNoise(1.0)
    player = Player()
    player.pause()
    player.queue(source)

    # Pause for the duration of the sound
    sleep(1.0)

    interactive.ask_question('Did you not hear any sound?')

@pytest.mark.requires_user_validation
def test_pause_sound(interactive):
    """Test that a playing sound can be paused."""
    source = procedural.WhiteNoise(60.0)
    player = Player()
    player.queue(source)
    player.play()

    sleep(1.0)
    player.pause()

    interactive.ask_question('Did you hear white noise for 1 second and is it now silent?')

    player.play()

    interactive.ask_question('Do you hear white noise again?')

    player.delete()

    interactive.ask_question('Is it silent again?')

@pytest.mark.requires_user_validation
def test_next_on_end_of_stream(interactive):
    """Test that multiple items on the queue are played after each other."""
    source1 = procedural.WhiteNoise(1.0)
    source2 = procedural.Sine(1.0)
    player = Player()
    player.queue(source1)
    player.queue(source2)
    player.play()

    sleep(2.0)
    interactive.ask_question('Did you hear white noise for 1 second and then a tone at 440 Hz (A above middle C)?')

@pytest.mark.requires_user_validation
def test_static_source_wrapping(interactive):
    """Test that a sound can be recursively wrappend inside a static source."""
    source = procedural.WhiteNoise(1.0)
    source = StaticSource(source)
    source = StaticSource(source)
    player = Player()
    player.queue(source)
    player.play()

    sleep(1.0)

    interactive.ask_question('Did you hear white noise for 1 second?')
