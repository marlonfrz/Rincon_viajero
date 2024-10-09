document.addEventListener('DOMContentLoaded', () => {
    const searchIcon = document.getElementById('search-icon');
    const searchModal = new bootstrap.Modal(document.getElementById('searchModal'));
    const searchInput = document.querySelector('input[name="query"]');

    searchIcon.addEventListener('click', () => {
      searchModal.show();
      searchInput.value = '';
    });
  });