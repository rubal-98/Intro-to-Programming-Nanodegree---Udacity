# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

conjuring = media.Movie("The Conjuring","The Conjuring is a 2013 American supernatural horror film","https://upload.wikimedia.org/wikipedia/en/thumb/1/1f/Conjuring_poster.jpg/220px-Conjuring_poster.jpg","https://www.youtube.com/watch?v=k10ETZ41q5o","TIME OF THE SEASON,SLEEP WALK","$320,070,008","Horror")
#cojuring.show_trailer()
the_fault_in_our_stars = media.Movie("The Fault in Our Stars","The Fault in Our Stars is a 2014 American romantic drama film","https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png","https://www.youtube.com/watch?v=9ItBvH5J6ss","All of the Stars,Simple as This,Let Me In","$307,166,834","Romantic-Drama")
#the_fault_in_our_stars.show_trailer()
insidious = media.Movie("Insidious","Insidious is a 2011 American supernatural horror film","https://upload.wikimedia.org/wikipedia/en/2/2d/Insidious_poster.jpg","https://www.youtube.com/watch?v=k10ETZ41q5o","TIPTOE THROUGH THE TULIPS","$189,814,155","Horror")
#insidious.show_trailer()
frozen = media.Movie("Frozen","Frozen is a 2013 American 3D computer-animated musical fantasy comedy-drama film","https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg","https://www.youtube.com/watch?v=TbQm5doF_Uc","LET IT GO,FROZEN HEART","$1,276,480,335","Animated")
#frozen.show_trailer()
ps_i_love_you = media.Movie("P.S. I Love You","P.S. I Love You is a 2007 American drama film","https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/PS_I_Love_You_%28film%29.jpg/220px-PS_I_Love_You_%28film%29.jpg","https://www.youtube.com/watch?v=CZzW6_hR068","LOVE YOU TILL THE END, SAME MISTAKE","$156,835,339","Drama")
#ps_i_love_you.show_trailer()
annabelle = media.Movie("Annabelle","Annabelle is a 2014 American supernatural horror film","http://t3.gstatic.com/images?q=tbn:ANd9GcQOlW5oFheta_jLvWYr__R8d1D7UqR3Vy8uhC2QzcZU7s9K4wdc","https://www.youtube.com/watch?v=paFgQNPGlsg","CHERISH,MORE TODAY THAN YESTERDAY","$256,873,813","Horror")
#annabelle.show_trailer()
movies = [conjuring, the_fault_in_our_stars, insidious, frozen, ps_i_love_you, annabelle]
fresh_tomatoes.open_movies_page(movies)
