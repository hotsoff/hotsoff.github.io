<?php
include 'header.php';
?>


<!DOCTYPE html>
<html>
<head>
    <title>Слайдер на PHP</title>
    <!-- Подключение стилей -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="slider">
        <?php
        // Подключение к базе данных
        $conn = mysqli_connect('localhost', 'root', '', 'slides');

        // Проверка соединения
        if (!$conn) {
            die("Ошибка подключения: " . mysqli_connect_error());
        }

        // Запрос к базе данных для получения данных о слайдах
        $sql = "SELECT * FROM slides";
        $result = mysqli_query($conn, $sql);

        // Обработка результатов запроса
        while ($row = mysqli_fetch_assoc($result)) {
            $id = $row['id'];
            $image = $row['image'];
            $title = $row['title'];
            $description = $row['description'];

            // Отображение слайда на веб-странице
            echo '<div class="slide">';
            echo '<img src="' . $image . '" alt="' . $title . '">';
            echo '<div class="slide-content">';
            echo '<h2>' . $title . '</h2>';
            echo '<p>' . $description . '</p>';
            echo '</div>';
            echo '</div>';
        }

        // Закрытие соединения с базой данных
        mysqli_close($conn);
        ?>
    </div>

    <!-- Подключение скриптов -->
    <script src="jquery.min.js"></script>
    <script src="slick.min.js"></script>
    <script>
        $(document).ready(function() {
            $('.slider').slick({
                autoplay: true,
                arrows: true,
                prevArrow: '<button type="button" class="slick-prev">Previous</button>',
                nextArrow: '<button type="button" class="slick-next">Next</button>',
                dots: true,
                infinite: true,
                speed: 500,
                fade: true,
                cssEase: 'linear'
            });
        });
    </script>
</body>
</html>
