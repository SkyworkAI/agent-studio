:py:mod:`agent_studio.envs.desktop_env.tools.keyboard`
======================================================

.. py:module:: agent_studio.envs.desktop_env.tools.keyboard


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.tools.keyboard.Keyboard




.. py:class:: Keyboard


   .. py:method:: type(text: str, interval: float | None = None) -> None

      Types a string of characters.

      :param text: The string to be typed out.
      :type text: str
      :param interval: The delay between pressing each
      :type interval: float, optional
      :param character key.:


   .. py:method:: press(keys: str | list[str], interval: float = 0.1) -> None

      Presses a key or a sequence of keys.

      :param keys: The key(s) to be pressed. If keys is a list, each key
                   in the list will be pressed once.
      :type keys: str or list
      :param interval: The delay between each key press.
      :type interval: float, optional


   .. py:method:: hotkey(keys: list[str], interval: float = 0.1) -> None

      Presses a sequence of keys in the order they are provided,
          and then release them in reverse order.

      :param keys: The keys to be pressed.
      :type keys: list
      :param interval: The delay between each key press.
      :type interval: float, optional


   .. py:method:: down(key: str)

      Presses down a key.


   .. py:method:: up(key: str)

      Releases a key.



