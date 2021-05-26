#This code was written by Shreeharan for the YouTube Channel Stark Intelligence
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = [] #movies dictionary


#add movie function
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({             #adding the input given by the user to the movies dictionary
            'title': title,
            'director': director,
            'year': year
    })

#show movies function
def show_movies():
    for movie in movies:
        print_movie(movie)


#print movie function
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Released Year: {movie['year']}")


#find movies function
def find_movies():
    search_title = input("Enter the movie title you are looking for: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


#menu function
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            show_movies()
        elif selection == "f":
            find_movies()
        elif selection == "q":
            break
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()