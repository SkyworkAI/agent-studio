:py:mod:`agent_studio.envs.desktop_env.tools.mouse`
===================================================

.. py:module:: agent_studio.envs.desktop_env.tools.mouse


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.tools.mouse.Mouse




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.tools.mouse.monitor


.. py:data:: monitor

   

.. py:class:: Mouse


   .. py:method:: scroll(clicks)

      Scrolls the mouse wheel up or down.


   .. py:method:: move(x: float | None = None, y: float | None = None)

      Moves the mouse cursor to the specified coordinates.


   .. py:method:: click(x: float | None = None, y: float | None = None, button='left', clicks=1, interval=0.0)

      Performs a click at the specified coordinates.


   .. py:method:: down()

      Presses the mouse button.


   .. py:method:: up()

      Releases the mouse button.



