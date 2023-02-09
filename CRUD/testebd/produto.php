<?php
use \yii\bootstrap5\ActiveForm;
use \yii\helpers\Html;
?>

<h2>Formulário de Registro dos Produtos</h2>
<hr>
<?php $form = \yii\bootstrap5\ActiveForm::begin() ?>
    <br>    
    <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fanamariabraga.globo.com%2Freceita%2Fbatata-frita-sequinha%2F&psig=AOvVaw1lTvWeoNiNqYeomVdbNW2e&ust=1676015160508000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNCF5pL5h_0CFQAAAAAdAAAAABAZ">
    <br>
    <button type="button" onclick="Evento()">Add carrinho</button>

    <script>
    function Evento(){
        define('nome', 'macarrão')
        alert('Adicionado ao carrinho')
    }
    </script>
    <br>
    <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fanamariabraga.globo.com%2Freceita%2Fbatata-frita-sequinha%2F&psig=AOvVaw1lTvWeoNiNqYeomVdbNW2e&ust=1676015160508000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCNCF5pL5h_0CFQAAAAAdAAAAABAZ">
    <br>
    <button type="button" onclick="Evento()">Add carrinho</button>

    <script>
    function Evento(){
        alert('Adicionado ao carrinho')
    }
    </script>
    <br>
    <img src="">
    <br>
    <button type="button" onclick="Evento()">Add carrinho</button>

    <script>
    function Evento(){
        alert('Adicionado ao carrinho')
    }
    </script>
    <br>
    <img src="">
    <br>
    <button type="button" onclick="Evento()">Add carrinho</button>

    <script>
    function Evento(){

        alert('Adicionado ao carrinho')
    }
    </script>
    
    <div class="form-group">
        <?= Html:: submitButton('Comprar',['class'=>'btn btn-primary']) ?>
    </div>
<?php ActiveForm::end() ?>
