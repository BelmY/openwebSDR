# -*- coding: utf-8 -*-

# ==== Server settings ====
web_port = 5000
# If this contains an incorrect value, the web UI may freeze on load (it can't open websocket)
server_hostname = "CRRP-SDR"
max_clients = 20

# ==== Web GUI configuration ====
receiver_name = "[Casa do Radioamador de Ribeirao Preto]"
receiver_location = "Ribeirão Preto SP, Brazil"
receiver_qra = "PY2ERA"
receiver_asl = 540
receiver_ant = "Windom"
receiver_device = "RTL-SDR"
receiver_admin = "Ricardo Paschoali (PY2PCR)"
receiver_gps = (47.000000, 19.000000)
photo_height = 350
photo_title = "Casa Do Radioamador de Ribeirao Preto-SP"
photo_desc = """
You can add your own background photo and receiver information.<br />
Receiver is operated by: <a href="mailto:%[RX_ADMIN]">%[RX_ADMIN]</a><br/>
Device: %[RX_DEVICE]<br />
Antenna: %[RX_ANT]<br />
Website: <a href="http://casadoradioamador.org.br" target="_blank">http://casadoradioamador.org.br</a>
"""

sdrhu_key = ""
# 3. Set this setting to True to enable listing:
sdrhu_public_listing = False

# ==== DSP/RX settings ====
fft_fps = 20
fft_size = 4096  # Should be power of 2
# If fft_voverlap_factor is above 0, multiple FFTs will be used for creating a line on the diagram.
fft_voverlap_factor = 0.3

# samp_rate = 250000
samp_rate = 900000
center_freq = 146670000
# in dB. For an RTL-SDR, rf_gain=0 will set the tuner to auto gain mode, else it will be in manual gain mode.
rf_gain = 30
ppm = 45
audio_compression = "adpcm"  # valid values: "adpcm", "none"
fft_compression = "adpcm"  # valid values: "adpcm", "none"

digimodes_enable = False  # Decoding digimodes come with higher CPU usage.
digimodes_fft_size = 1024

start_rtl_thread = True

"""
Note: if you experience audio underruns while CPU usage is 100%, you can: 
- decrease `samp_rate`,
- set `fft_voverlap_factor` to 0,
- decrease `fft_fps` and `fft_size`,
- limit the number of users by decreasing `max_clients`.
"""
# ==== I/Q sources ====
# (Uncomment the appropriate by removing # characters at the beginning of the corresponding lines.)

#################################################################################################
# Is my SDR hardware supported?                                                                 #
# Check here: https://github.com/simonyiszk/openwebrx/wiki#guides-for-receiver-hardware-support #
#################################################################################################

# You can use other SDR hardware as well, by giving your own command that outputs the I/Q samples... Some examples of configuration are available here (default is RTL-SDR):

# >> RTL-SDR via rtl_sdr
start_rtl_command = "rtl_sdr -s {samp_rate} -f {center_freq} -p {ppm} -g {rf_gain} -".format(
    rf_gain=rf_gain, center_freq=center_freq, samp_rate=samp_rate, ppm=ppm)
format_conversion = "csdr convert_u8_f"

# lna_gain=8
# rf_amp=1
#start_rtl_command="hackrf_transfer -s {samp_rate} -f {center_freq} -g {rf_gain} -l{lna_gain} -a{rf_amp} -r-".format(rf_gain=rf_gain, center_freq=center_freq, samp_rate=samp_rate, ppm=ppm, rf_amp=rf_amp, lna_gain=lna_gain)
#format_conversion="csdr convert_s8_f"
"""
To use a HackRF, compile the HackRF host tools from its "stdout" branch:
 git clone https://github.com/mossmann/hackrf/
 cd hackrf
 git fetch
 git checkout origin/stdout
 cd host
 mkdir build
 cd build
 cmake .. -DINSTALL_UDEV_RULES=ON
 make
 sudo make install
"""

# ==== Misc settings ====

shown_center_freq = center_freq  # you can change this if you use an upconverter

client_audio_buffer_size = 5
# increasing client_audio_buffer_size will:
# - also increase the latency
# - decrease the chance of audio underruns

start_freq = center_freq
start_mod = "nfm"  # nfm, am, lsb, usb, cw

# TCP port for ncat to listen on. It will send I/Q data over its connections, for internal use in OpenWebRX. It is only accessible from the localhost by default.
iq_server_port = 4951

#access_log = "~/openwebrx_access.log"

# ==== Color themes ====

# A guide is available to help you set these values: https://github.com/simonyiszk/openwebrx/wiki/Calibrating-waterfall-display-levels

# default theme by teejez:
#waterfall_colors = "[0x000000ff,0x2e6893ff, 0x69a5d0ff, 0x214b69ff, 0x9dc4e0ff,  0xfff775ff, 0xff8a8aff, 0xb20000ff]"
waterfall_colors = "[0x000000ff,0x0000ffff,0x00ffffff,0x00ff00ff,0xffff00ff,0xff0000ff,0xff00ffff,0xffffffff]"
waterfall_min_level = -90  # in dB
waterfall_max_level = -20
waterfall_auto_level_margin = (5, 40)
# old theme by HA7ILM:
# waterfall_min_level = -115 #in dB
#waterfall_max_level = 0
#waterfall_auto_level_margin = (20, 30)
# For the old colors, you might also want to set [fft_voverlap_factor] to 0.

# Note: When the auto waterfall level button is clicked, the following happens:
#   [waterfall_min_level] = [current_min_power_level] - [waterfall_auto_level_margin[0]]
#   [waterfall_max_level] = [current_max_power_level] + [waterfall_auto_level_margin[1]]
#
#   ___|____________________________________|____________________________________|____________________________________|___> signal power
#        \_waterfall_auto_level_margin[0]_/ |__ current_min_power_level          | \_waterfall_auto_level_margin[1]_/
#                                                      current_max_power_level __|

# 3D view settings
mathbox_waterfall_frequency_resolution = 128  # bins
mathbox_waterfall_history_length = 5  # seconds
mathbox_waterfall_colors = "[0x000000ff,0x2e6893ff, 0x69a5d0ff, 0x214b69ff, 0x9dc4e0ff,  0xfff775ff, 0xff8a8aff, 0xb20000ff]"

# === Experimental settings ===
# Warning! The settings below are very experimental.
# This allows you to change the buffering mode of csdr.
csdr_dynamic_bufsize = False
# This prints the buffer sizes used for csdr processes.
csdr_print_bufsizes = True
# Setting this True will print out how much data is going into the DSP chains.
csdr_through = True

# in megabytes. This sets the approximate size of the circular buffer used by nmux.
nmux_memory = 100
