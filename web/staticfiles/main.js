const editButtons = document.querySelectorAll(".edit-button");
editButtons.forEach((button) => {
    button.addEventListener("click", function () {
        const userId = button.getAttribute("data-user-id");
        const editForm = document.getElementById("edit-form");
        const editUserModal = document.getElementById("editUserModal");
        const closeBtn = document.querySelector(".close");

        // Xử lý sự kiện khi nút "Edit" được nhấn
        editForm.action = `/edit_user/${userId}/`;
        editUserModal.style.display = "block";

        // Đóng modal khi nút đóng được nhấn
        closeBtn.addEventListener("click", function () {
            editUserModal.style.display = "none";
        });

        // Đóng modal khi người dùng click bên ngoài modal
        window.addEventListener("click", function (event) {
            if (event.target == editUserModal) {
                editUserModal.style.display = "none";
            }
        });
    });
});
