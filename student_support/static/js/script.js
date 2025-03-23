function fetchStudents() {
    fetch('/api/students/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const studentList = document.getElementById('student-list');
            studentList.innerHTML = ''; // Очистить список перед добавлением новых данных

            data.forEach(student => {
                const listItem = document.createElement('li');
                listItem.textContent = `${student.name} - ${student.id}`; // Предполагается, что у студента есть свойства name и id
                studentList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

// Вызов функции для получения данных при загрузке страницы
document.addEventListener('DOMContentLoaded', fetchStudents);
