echo "Checking bluetooth service status..."
service bluetooth status
echo "Now to scan for the Wiimote..."
echo "Press 1 and 2 on your Wiimote TOGETHER, release and then press ENTER"
read ans
echo "You should see your device come up during the scan"
hcitool scan
