:py:mod:`agent_studio.envs.desktop_env.vnc_client`
==================================================

.. py:module:: agent_studio.envs.desktop_env.vnc_client


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.vnc_client.Position
   agent_studio.envs.desktop_env.vnc_client.Clipboard
   agent_studio.envs.desktop_env.vnc_client.Screen
   agent_studio.envs.desktop_env.vnc_client.Video
   agent_studio.envs.desktop_env.vnc_client.UpdateType
   agent_studio.envs.desktop_env.vnc_client.VNCClient
   agent_studio.envs.desktop_env.vnc_client.VNCFrame
   agent_studio.envs.desktop_env.vnc_client.VNCStreamer
   agent_studio.envs.desktop_env.vnc_client.LocalStreamer



Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.vnc_client.read_int
   agent_studio.envs.desktop_env.vnc_client.read_text
   agent_studio.envs.desktop_env.vnc_client.skip_to_eof
   agent_studio.envs.desktop_env.vnc_client.pack_ard



Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.vnc_client.logger
   agent_studio.envs.desktop_env.vnc_client.screen_ratios
   agent_studio.envs.desktop_env.vnc_client.video_modes


.. py:data:: logger

   

.. py:data:: screen_ratios
   :type: set[fractions.Fraction]

   

.. py:data:: video_modes
   :type: dict[bytes, str]

   

.. py:function:: read_int(reader: asyncio.StreamReader, length: int) -> int
   :async:

   Reads, unpacks, and returns an integer of *length* bytes.


.. py:function:: read_text(reader: asyncio.StreamReader, encoding: str) -> str
   :async:

   Reads, unpacks, and returns length-prefixed text.


.. py:function:: skip_to_eof(reader: asyncio.StreamReader)
   :async:


.. py:function:: pack_ard(data)


.. py:class:: Position


   .. py:attribute:: width
      :type: int

      

   .. py:attribute:: height
      :type: int

      


.. py:class:: Clipboard


   Shared clipboard.

   .. py:attribute:: writer
      :type: asyncio.StreamWriter

      

   .. py:attribute:: text
      :type: str
      :value: ''

      

   .. py:method:: write(text: str)

      Sends clipboard text to the server.



.. py:class:: Screen


   .. py:property:: slices
      :type: tuple[slice, slice]

      Object that can be used to crop the video buffer to this screen.

   .. py:property:: score
      :type: float

      E501
      is proportional to its pixel area. For non-standard aspect ratios, the score is further multiplied by the ratio  # noqa: E501
      or its reciprocal, whichever is smaller.

      :type: A measure of our confidence that this represents a real screen. For screens with standard aspect ratios, this  # noqa

   .. py:attribute:: x
      :type: int

      

   .. py:attribute:: y
      :type: int

      

   .. py:attribute:: width
      :type: int

      

   .. py:attribute:: height
      :type: int

      


.. py:class:: Video


   .. py:attribute:: reader
      :type: asyncio.StreamReader

      

   .. py:attribute:: writer
      :type: asyncio.StreamWriter

      

   .. py:attribute:: decompress
      :type: Callable[[bytes], bytes]

      

   .. py:attribute:: name
      :type: str

      

   .. py:attribute:: width
      :type: int

      

   .. py:attribute:: height
      :type: int

      

   .. py:attribute:: mode
      :type: str

      

   .. py:attribute:: data
      :type: numpy.ndarray | None

      

   .. py:attribute:: bypp
      :value: 4

      

   .. py:attribute:: now_encoding
      :type: str | None

      

   .. py:method:: create(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> Video
      :classmethod:
      :async:


   .. py:method:: refresh(x: int = 0, y: int = 0, width: int | None = None, height: int | None = None)

      Sends a video buffer update request to the server.


   .. py:method:: read()
      :async:


   .. py:method:: as_rgba() -> numpy.ndarray

      Returns the video buffer as a 3D RGBA array.


   .. py:method:: is_complete()

      Returns true if the video buffer is entirely opaque.



.. py:class:: UpdateType


   Bases: :py:obj:`enum.Enum`

   Update from server to client.

   .. py:attribute:: VIDEO
      :value: 0

      

   .. py:attribute:: CLIPBOARD
      :value: 2

      


.. py:class:: VNCClient


   .. py:attribute:: reader
      :type: asyncio.StreamReader

      

   .. py:attribute:: writer
      :type: asyncio.StreamWriter

      

   .. py:attribute:: clipboard
      :type: Clipboard

      

   .. py:attribute:: video
      :type: Video

      

   .. py:attribute:: host_key
      :type: cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey | None

      

   .. py:method:: create(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, username: str | None = None, password: str | None = None, host_key: cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey | None = None) -> VNCClient
      :classmethod:
      :async:


   .. py:method:: read() -> UpdateType | None
      :async:


   .. py:method:: screenshot(x: int = 0, y: int = 0, width: int | None = None, height: int | None = None) -> numpy.ndarray
      :async:


   .. py:method:: disconnect() -> None
      :async:



.. py:class:: VNCFrame(parent, size_hint: PyQt6.QtCore.QSize, enable_selection: bool = False)


   Bases: :py:obj:`PyQt6.QtWidgets.QLabel`

   The VNC frame for rendering the VNC screen.

   .. py:method:: reset()


   .. py:method:: get_cursor_pos()


   .. py:method:: mousePressEvent(event)

      Capture the starting point of the selection.


   .. py:method:: mouseMoveEvent(event)

      Update the selection end point and repaint the widget.


   .. py:method:: mouseReleaseEvent(event)

      Finalize the selection on mouse release.


   .. py:method:: paintEvent(event)


   .. py:method:: get_selection() -> tuple[int, int, int, int] | None

      Return the coordinates of the selection.


   .. py:method:: update(qimage)



.. py:class:: VNCStreamer(env_server_addr: str, vnc_port: int, vnc_password: str)


   .. py:method:: start() -> None


   .. py:method:: stop()


   .. py:method:: connect_vnc()
      :async:

      Connects to VNC server.


   .. py:method:: between_callback()


   .. py:method:: reconnect()
      :async:


   .. py:method:: get_current_frame() -> numpy.ndarray | None



.. py:class:: LocalStreamer(monitor_idx: int)


   .. py:method:: start() -> None


   .. py:method:: stop()


   .. py:method:: get_current_frame() -> numpy.ndarray | None



