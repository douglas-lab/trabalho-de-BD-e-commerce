<?php 

namespace app\models;

use yii\db\ActiveRecord;

class TestebdModel extends ActiveRecord
{
    public $nome;
    public $valor;
    public $especificacao;
    public $categoria;

   
    public function attributeLabels()
    {
        return[
            'nome' => 'Nome do produto',
            'valor' => 'Preço',
            'especificacao' => 'Especificacao',
            'categoria' => 'Categoria'
        ];
    }
}