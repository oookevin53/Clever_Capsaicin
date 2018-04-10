# Clever Capsaicin

Clever Capsaicin is a recommendation engine built to bring you out of your comfort zone. Find and discover new hot sauces that were made *just* for your taste buds!

## Table of Contents

- [Introduction](#introduction)
- [Data Collection](#data-collection)
- [Content-based vs Collaborative Filtering](#content-based-vs-collaborative-filtering)
- [K-Nearest Neighbors](#k-nearest-neighbors)
- [Cosine Similarity](#cosine-similarity)
- [Results / Demo](#results--demo)
- [Visualization using t-SNE](#visualization-using-t-sne)
- [What's Next?](#whats-next)
- [References](#references)

## Introduction:

All I knew was Sriracha (or Rooster Sauce as I've seen it called) growing up. Whether I'm having a bowl of noodles or a bacon, egg, and cheese breakfast sandwich, you'd know I was putting Sriracha on it. As I began to venture deeper into the hot sauce world, I became more familiar with the household names like Tabasco, Frank's or Cholula, but, in my opinion, none of them were quite the same. I always found myself circling back to Sriracha.

![alt text](https://github.com/oookevin53/Clever_Capsaicin/blob/master/images/common_sauces.png "Look familiar?")

I recently discovered a Youtube series called "Hot Ones." The underlying theme of the show is an interview of celebrities while eating chicken wings covered in hot sauce that becomes progressively hotter and hotter. It was only natural me to open this Pandora's box as the show had introduced many new "artisanal" sauces I had never seen before.

<img src="https://github.com/oookevin53/Clever_Capsaicin/blob/master/images/hot_ones.png" width="250" />

That brings me to the motivation of this project. If any hot sauce enthusiast out there is like me, then you're always struggling to fight the masochist in you while seeking a balance of heat and flavor. How do I find hot sauces like Sriracha but hotter and lesser-known?

Even if you don't have a high tolerance for spicy food or suddenly feel like stepping out of your comfort zone, you only have to like 1 sauce for a recommendation. After all, everybody could use a little extra spice in life.

## Data Collection:

The images and metadata used in the this project were scraped from [Heat Hot Sauce Shop](https://heathotsauce.com/) and [Amazon](https://www.amazon.com/) (sorry if you're reading this).

The features used include:
- Ingredients (type of peppers used, fruits, etc.)
- Flavor profile (smoky, sweet, tangy, etc.)
- Heat level (subjective - 5 levels: Extreme, Extra Hot, Hot, Mild, Medium)
- If the sauce was featured on a show/blog

### Challenges:

1. A challenge I came across when cleaning the data was the ingredients labels had different names for the same type of pepper. An example of this would be the infamous ghost pepper. Another name for the ghost pepper is bhuk jolokia. Another example is the hatch chile pepper. While some would argue they are different because of the location they're grown, for the purpose of this project, hatch chiles are synonymous for Anaheim peppers or New Mexico chiles.
2. Lack of user Data - Explained in [Content-based vs Collaborative Filtering](#content-based-vs-collaborative-filtering) section
3. How to score recommendations?

## Content-based vs Collaborative Filtering:

explain both types and differences and why content is better
hot sauce recommendations using content vs collaborative

## K-Nearest Neighbors:

## Cosine Similarity:

## Results / Demo:

## Visualization using t-SNE:

## What's Next?

## References:

- http://infolab.stanford.edu/~ullman/mmds/ch9.pdf
- https://beckernick.github.io/law-clustering/
- http://blog.untrod.com/2016/06/simple-similar-products-recommendation-engine-in-python.html
