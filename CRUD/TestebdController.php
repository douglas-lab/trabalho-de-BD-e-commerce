<?php

namespace app\controllers;

use app\models\TestebdModel;
use Yii;
use yii\base\Controller;

class TestebdController extends Controller{
    public function actionProduto()
    {
        $testebdModel = new TestebdModel;
        $post = Yii::$app->request->post();
        
        if($testebdModel->load($post) && $testebdModel->validate()){
            return $this->render('compra', [
                'model' => $testebdModel
            ]);
        }else{
            return $this->render('produto', [
                'model' => $testebdModel]);
            }
    }
}