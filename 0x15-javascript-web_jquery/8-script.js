$.ajax({
    method: "GET",
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    dataType: "json",
    success: function(data) {
        let movieTitles = data.results.map(function(movie) {
            return movie.title;
        });
        let movieList = $("ul#list_movies");
        $.each(movieTitles, function(index, title) {
            let listMovie = $("<li>" + title + "</li>");
            movieList.append(listMovie);
        });
    }
});
