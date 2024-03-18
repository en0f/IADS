# IADS
Internal Application Discovery Service

Written by en0f

This application creates a simple GUI with a text entry field for the subnet, a "Scan" button, and a text area to display the results. When the "Scan" button is clicked, the run_scan method is called, which validates the input subnet and starts a new thread to run the scan_subnet method.

The scan_subnet method runs the masscan command with the specified subnet and ports 1-10000, along with the --http-get option to send an HTTP GET request to each open port. The output of masscan is captured and displayed directly in the text area of the GUI.

This application will display all the results from masscan, including the hosts that did not respond to the HTTP GET request. The output will include information about open ports, banners, and other details provided by masscan.

Note that this code assumes you have masscan installed and accessible from the command line. Additionally, it uses the tun0 interface for scanning, which you may need to adjust based on your system configuration.
