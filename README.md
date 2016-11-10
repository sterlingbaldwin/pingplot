# pingplot
A tiny utility to graph your network ping time to a given host

# install
`git clone https://github.com/sterlingbaldwin/pingplot.git
cd pingplot
pip install -r requirements.txt
`
# usage
./pingplot.py --host <some.host.name.org>

To kill the plot, close the matplot window. Any 0 times mean the packet was dropped.
