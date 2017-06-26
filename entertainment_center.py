# Importing the media module to use the Movie class
import media
# Importing fresh_tomatoes module which contains the html and some functions
import fresh_tomatoes

# Defining instances of the Movie class
logan = media.Movie(
    "Logan",
    "Story of wolverine and the mutants"
    "with special abilities.",
	"https://www.flickeringmyth.com/wp-content/uploads/2017/01/logan-movie-poster.png",  # NOQA
    "https://www.youtube.com/watch?v=Div0iP65aZo"
    )

gravity = media.Movie(
    "Gravity",
    "A story based on space travels as the name suggests.",
    "http://blog.hotelbloom.com/wp-content/uploads/2013/10/gravity.jpg",  # NOQA
    "https://www.youtube.com/watch?v=OiTiKOy59o4"
    )

breaking_bad = media.Movie(
    "Breaking Bad",
    "Story of a chemist who turns to a drug dealer"
    "to make money for his family's future when he finds out he has cancer.",
    "https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png",  # NOQA
    "https://www.youtube.com/watch?v=HhesaQXLuRY"
    )

gameofthrones = media.Movie(
    "A Game of Thrones",
    "The story of the seven kingdoms"
    "and the iron throne entailing white walkers"
    "and devastating deaths(mostly of your favourite character.",
    "http://static1.businessinsider.com/image/56ce04c6dd0895d9048b4772/why-these-new-game-of-thrones-posters-reveal-more-than-you-think.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1Mlhnt0jMlg"
    )

friends = media.Movie(
    "Friends",
    "Story of 6 friends who teach us to live freely,"
    "laugh often and help unconditionaly",
    "https://s-media-cache-ak0.pinimg.com/736x/15/c4/da/15c4da03bc524af9b91ee676519b12b1.jpg",  # NOQA
    "https://www.youtube.com/watch?v=bvEnlf9g4co"
    )

now_you_see_me = media.Movie(
    "Now you see me",
    "Story of the world's greatest magicians.",
    "http://is5.mzstatic.com/image/thumb/Video18/v4/74/33/ac/7433ace5-71f4-2163-1bdc-c047939edf3b/source/1200x630bb.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KzJNYYkkhzc"
    )

# A list of instances assigned to the movies variable
movies = [logan, gravity, gameofthrones, breaking_bad, friends, now_you_see_me]
# Calling the function to open the movie
# website contained in the fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
