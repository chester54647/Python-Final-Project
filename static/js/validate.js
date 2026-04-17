function validateForm() {
    let title = document.getElementById("title").value;
    let genre = document.getElementById("genre").value;
    let platform = document.getElementById("platform").value;
    let rating = document.getElementById("rating").value;
    let image = document.getElementById("image").value;

    if (title === "" || genre === "" || platform === "" || rating === "") {
        alert("All text fields must be filled out.");
        return false;
    }

    if (image === "") {
        alert("Please select an image file.");
        return false;
    }

    return true;
}