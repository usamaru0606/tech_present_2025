# サーバー処理

## アプリ起動方法

1. app_serverディレクトリに移動する
2. 「python -m app」コマンドを起動する

## キーの設定
1. import.iniにキーとついでに、データベースのURLをコピーする
2. config.pyをプルしたのち、.envファイルにペーストする

## 機械学習（忘れないように...）
1. insert_health.py　               ：国民健康データから身長・体重・運動量のsample_userテーブルに保存
2. weight_loss_data.py              ：ランダムのパーソナル情報を作成し、体重減少量を作成してCSV（仮想データ）に保存
3. model_train.py                   ：仮想データから身長・体重・運動量から体重減少量を予測する機械学習モデルを作成
4. predict_target_weight.py         ：sample_userテーブルのデータに機械学習モデルで体重減少量を予測してsample_userテーブルに追加登録
5. model_total_weekly_exercise.py   ：sample_userテーブルから身長・体重・体重減少量から運動量を予測する機械学習モデルを作成
6. predict_total_weekly_exercise.py ：実際の特定ユーザーだけ運動量を予測し、DBに登録　※FastAPIでidを指定したい
7. gpt_traininigmenu.py             ：ユーザー情報を DB から取得して GPT に運動メニューを依頼してtraining_menuテーブルに登録
8. gpt_mealmenu.py                  ：ユーザー情報を DB から取得して GPT に食事メニューを依頼してmeal_menuテーブルに登録
9. 未作成                          　：フロントに運動メニューと食事メニューを返す。
