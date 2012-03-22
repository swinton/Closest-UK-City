# About

Simple web app to return the closest UK city to a set of co-ordinates.

E.g.

<pre>
$ curl http://127.0.0.1:5000/get_closest_city/50.828869/-0.13414
{

    "city": "Brighton",
    "city_lat": 50.828869,
    "dist": 1.4901161193847656e-8,
    "city_lng": -0.13414

}
</pre>

# Installation

<pre>
$ pip install requirements.txt
</pre>

# Usage

<pre>
$ python webapp.py
$ curl http://127.0.0.1:5000/get_closest_city/&lt;lat&gt;/&lt;lng&gt;
</pre>

Command line usage is also possible - but you can work that out for yourself ;)

# Feedback

@[steveWINton](http://twitter.com/steveWINton)