Duplicator is an open source tool made to help test the size limits of a shopping cart.
The tool will take a file in and duplicate the contents a user-defined number of times.

Key uses:<br />
-f &nbsp;&nbsp;&nbsp;&nbsp;Path to the input file<br />
-v &nbsp;&nbsp;&nbsp;&nbsp;verbose mode<br />
-o &nbsp;&nbsp;&nbsp;&nbsp;output file<br />
-r &nbsp;&nbsp;&nbsp;&nbsp;number of times the input should be duplicated<br />
-s &nbsp;&nbsp;&nbsp;&nbsp;a starting index number<br />
-d &nbsp;&nbsp;&nbsp;&nbsp;a defined delimiter to separate the duplicated entries, default is ,<br />

Example usage:
<pre>
  py duplicator.py -f input.txt -o output.txt -d , -r 2 -s 2
</pre>

<pre>
  input.txt
  {
    "id":%n%.
    "price":10.00.
    "description":"test"
  }
</pre>

<pre>
  output
  {
    "id":2.
    "price":10.00.
    "description":"test"
  },
  {
    "id":3.
    "price":10.00.
    "description":"test"
  }
</pre>
