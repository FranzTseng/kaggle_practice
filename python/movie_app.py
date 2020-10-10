# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def movie_list():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def show_movie():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")



def find_movie():
    search = input("Search for movies: ")
    for movie in movies:
        if movie['title']==search:
            print_movie(movie)
        else:
            pass

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            movie_list()
        elif selection == "l":
            show_movie()
        elif selection == "f":
            find_movie()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu()
