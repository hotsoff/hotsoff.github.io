<?php
include 'header.php';
?>

<!DOCTYPE html>
<html>
<head>
    <title>Название сайта</title>
</head>
<body style="background-color:  #E5EEF5;">
    <div class = 'container'>
        <h1 align="left" class= 'left'>Наши основные продукты</h1>
    </div>
      <div class = 'products-wrapper'>
        <?php
          for($i = 0; $i < 9; $i++):
        ?>
        <div class="skill">
            <div class="skill-title">
                <img src="img/product.jpg" alt="" class="title-img">
                  <h4 class="title">Название продукта</h4>
            </div>
                <ul class="in_title">
                  <li><p>Описание</p></li>
                  <li><p>Описание</p></li>
                  <li><p>Описание</p></li>
                </ul>
                <div class="actions">
                  <a href="">В корзину</a>
				        </div>
              </div>
        <?php endfor ?>
      </div>
</body>

<?php
include 'footer.php';
?>
</html>
