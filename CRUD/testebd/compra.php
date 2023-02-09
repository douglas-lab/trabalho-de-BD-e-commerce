<?php
?>
<p>Você inseriu as seguintes informações do Produto:</p>

<ul>
    <li><label>Nome do Produto</label>: <?= $model->nome ?></li>
    <li><label>Preço do Produto</label>:R$ <?= $model->valor ?></li>
    <li><label>Especificação do Produto</label>: <?= $model->especificacao ?></li>
    <li><label>Categoria do Produto</label>: <?= $model->categoria ?></li>
</ul>