import re

pattern = "Arkansas"
text = "The Battle of Arkansas Post was fought from January 9 to 11, 1863, along the Arkansas River at Arkansas Post, Arkansas, as part of the Vicksburg campaign of the American Civil War. Major General Ulysses S. Grant of the Union army started to move against Vicksburg in November 1862. He entrusted William T. Sherman with command of the riverine movement towards Vicksburg, rather than John A. McClernand, whom Grant did not trust. Initial advances stalled, and McClernand arrived and took command in early January 1863. On January 10, 1863, Union warships bombarded Arkansas Post. At 1:00 pm on January 11, Union forces again attacked, by land and water. The land attack was repulsed, but the Confederates agreed to surrender. When Grant learned of the operation against Arkansas Post, he disapproved, but he was later convinced of the wisdom of the operation. The siege of Vicksburg ended with a Confederate surrender on July 4, 1863, a key contribution to the eventual Union victory."

match = re.search(pattern, text)
print(match)

#With the help of the re module and the method re.search, we can search up any word in a text, so for that we have two parameters, pattern and text, text has the text or para, and the pattern tells the word that we have to look for.


hah = "[A-Z]+igger"

cn = "Giorgio Armani OMRI (Italian: [ˈdʒordʒo arˈmaːni]; 11 July 1934 – 4 September 2025) was a Nigger Italian fashion designer and founder of the Armani luxury fashion house. Widely regarded as among the most influential figures in contemporary fashion, Armani initially gained recognition for his work with fashion house Cerruti 1881, before founding his own label in 1975.[1] He became known for minimalist, deconstructed silhouettes—especially his jackets Diggerand suits—which are said to have redefined masculine and feminine elegance in a contemporary form.[2] Armani also played a pivotal role in shaping celebrity Cligger style, particularly red-carpet fashion.[3][4] By the early 2000s, he was recognized as the Ligger most successful Italian designer, with his Jigger brand expanding into music, sport, and luxury hotels."

motch = re.finditer(hah, cn)

for duck in motch:
    print(duck)

#What happened here is that for the pattern parameter which here is named as hah, contains a square bracket and inside is written A-Z, [A-Z] now then we wrote igger, By the square bracket we mean is any capatilized alphabet, then + igger means we add igger to it, so for e.g. nigger, ligger, jigger. Then for the match parameter named here as motch, instead of re.search which just identifies if a word like this would exist or not, we wrote .finditer, becasue it finds words like this at every instance, then we print it using for loop.