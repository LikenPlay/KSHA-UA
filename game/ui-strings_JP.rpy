init -2 python:
    init_language('jp')
    jpfont = 'font/VL-PGothic-Regular.ttf'
    def jpw(string):
        return (((('{font=') + (jpfont)) + ('}')) + (string)) + ('{/font} ')
    displayDict['jp'].styleoverrides = {'font':jpfont, 'language':'eastasian', 'line_spacing':-(3)}
    displayDict['jp'].timeformat = '%m/%d, %H:%M'
    displayDict['jp'].selector_padding = -(1)
    displayDict['jp'].nvl_paragraph_distance = 10
    displayDict['jp'].sayfont = jpfont
    displayDict['jp'].quote_outer_open = u"「"
    displayDict['jp'].quote_outer_close = u"」"
    displayDict['jp'].quote_inner_open = u"『"
    displayDict['jp'].quote_inner_close = u"』"
    displayDict['jp'].activeLanguage = jpw(u"日本語")
    displayDict['jp'].allLanguages = {}
    displayDict['jp'].allLanguages['en'] = jpw(u"英語")
    displayDict['jp'].allLanguages['fr'] = jpw(u"フランス語")
    displayDict['jp'].allLanguages['es'] = jpw(u"スペイン語")
    displayDict['jp'].allLanguages['jp'] = displayDict['jp'].activeLanguage
    displayDict['jp'].allLanguages['ru'] = jpw(u"ロシア語")
    displayDict['jp'].act_term = u"Act"
    displayDict['jp'].window_name = u"かたわ少女"
    displayDict['jp'].main_menu_start = u"はじめから"
    displayDict['jp'].main_menu_load = u"つづきから"
    displayDict['jp'].main_menu_extra = u"おまけ"
    displayDict['jp'].main_menu_config = u"環境設定"
    displayDict['jp'].main_menu_quit = u"終了"
    displayDict['jp'].game_menu_return = u"戻る"
    displayDict['jp'].game_menu_show = u"ウインドウ消去"
    displayDict['jp'].game_menu_history = u"テキストログ"
    displayDict['jp'].game_menu_skip = u"スキップ"
    displayDict['jp'].game_menu_auto = u"オート"
    displayDict['jp'].game_menu_config = u"環境設定"
    displayDict['jp'].game_menu_save = u"セーブ"
    displayDict['jp'].game_menu_load = u"ロード"
    displayDict['jp'].game_menu_main = u"タイトル"
    displayDict['jp'].game_menu_quit = u"ゲーム終了"
    displayDict['jp'].XstringClose = u"閉じる"
    displayDict['jp'].game_menu_current_scene = u"現在のシーン"
    displayDict['jp'].game_menu_current_music = u"BGM"
    displayDict['jp'].game_menu_replay_indicator = u"リプレイ"
    displayDict['jp'].return_button_text = u"戻る"
    displayDict['jp'].hdisabled_label = u"成人向けコンテンツ無効"
    displayDict['jp'].config_page_caption = u"環境設定"
    displayDict['jp'].config_fullscreen_label = u"フルスクリーンモード"
    displayDict['jp'].config_transitions_label = u"画面効果オフ"
    displayDict['jp'].config_skip_unseen_label = u"未読テキストもスキップ"
    displayDict['jp'].config_skip_after_choice_label = u"選択肢の後もスキップ継続"
    displayDict['jp'].config_textspeed_label = u"テキスト表示速度"
    displayDict['jp'].config_afmspeed_label = u"オートモード待ち時間"
    displayDict['jp'].config_musicvol_label = u"BGM音量"
    displayDict['jp'].config_musicvol_jukebox_label = u"音量"
    displayDict['jp'].config_fontsize_label = u"文字サイズ"
    displayDict['jp'].config_sfxvol_label = u"SE音量"
    displayDict['jp'].config_sfxtest_label = u"テスト"
    displayDict['jp'].config_gamepad_label = u"ゲームパッド設定…"
    displayDict['jp'].config_language_sel = jpw(u"言語選択…")
    displayDict['jp'].config_language_caption = jpw(u"設定 > 言語選択")
    displayDict['jp'].config_language_restart_note = jpw(u"注意：セッション中に言語を変更すると、ゲーム進行が章の最初に戻ります。")
    displayDict['jp'].gamepad_caption = u"設定 > ゲームパッド設定"
    displayDict['jp'].gamepad_key_na = u"未定義"
    displayDict['jp'].gamepad_request_key = u"“%s” に割り当てる\nボタンを押して下さい\nセレクトボタンまたは\nクリックで解除します"
    displayDict['jp'].yesno_yes = u"はい"
    displayDict['jp'].yesno_no = u"いいえ"
    displayDict['jp'].yesno_okay = u"続ける"
    displayDict['jp'].yesno_savesuccess = u"\nセーブが完了しました。"
    displayDict['jp'].yesno_quit = u"\nゲームを終了しますか？"
    displayDict['jp'].yesno_return_to_main = u"\nタイトル画面に戻りますか？"
    displayDict['jp'].save_page_caption = u"セーブ"
    displayDict['jp'].new_save_button = u"状態をセーブする"
    displayDict['jp'].load_page_caption = u"ロード"
    displayDict['jp'].yesno_load_in_game = u"状態が失われますが\nよろしいですか？"
    displayDict['jp'].yesno_save_overwrite = u"セーブデータを上書きしても\nよろしいですか？"
    displayDict['jp'].yesno_delete_savegame = u"このデータを削除しても\nよろしいですか？"
    displayDict['jp'].play_time_label = u"経過時間"
    displayDict['jp'].show_manual_saves = u"手動"
    displayDict['jp'].show_auto_saves = u"自動"
    displayDict['jp'].text_history_caption = u"テキストログ"
    displayDict['jp'].text_history_note = u"メモ"
    displayDict['jp'].extra_menu_caption = u"おまけ"
    displayDict['jp'].extra_music_button_label = u"音楽室"
    displayDict['jp'].extra_gallery_button_label = u"美術室"
    displayDict['jp'].extra_scene_button_label = u"図書室"
    displayDict['jp'].extra_omake_button_label = u"おまけ"
    displayDict['jp'].extra_opening_button_label = u"視聴覚室"
    displayDict['jp'].commentary_label = u"コメンタリー表示"
    displayDict['jp'].video_page_caption = u"おまけ > 視聴覚室"
    displayDict['jp'].music_page_caption = u"おまけ > 音楽室"
    displayDict['jp'].music_stop_button_text = u"停止"
    displayDict['jp'].music_now_playing = u"演奏中"
    displayDict['jp'].gallery_page_caption = u"おまけ > 美術室"
    displayDict['jp'].gallery_onelocked = u"残りCG：1"
    displayDict['jp'].gallery_manylocked = u"残りCG：%d"
    displayDict['jp'].gallery_singlelocked = u"CG %d / %d はロックされています"
    displayDict['jp'].gallery_num_page_prefix = u"{size=17}ページ {/size}"
    displayDict['jp'].gallery_num_page_error = u"表示するCGがありません"
    displayDict['jp'].scene_page_caption = u"おまけ > 図書室"
    displayDict['jp'].scene_completion_label = u"進捗率: %s%%"
    displayDict['jp'].scene_playthrough_label = u"リプレイフローを使用 (推奨)"
    displayDict['jp'].scene_launch_path = u"ルートを最初から\n開始しますか？"
    displayDict['jp'].joy_left = u"左"
    displayDict['jp'].joy_right = u"右"
    displayDict['jp'].joy_up = u"上"
    displayDict['jp'].joy_down = u"下"
    displayDict['jp'].joy_dismiss = u"選択／読む"
    displayDict['jp'].joy_rollback = u"テキストログ"
    displayDict['jp'].joy_holdskip = u"押している間スキップ"
    displayDict['jp'].joy_toggleskip = u"スキップモード"
    displayDict['jp'].joy_hide = u"ウインドウ消去"
    displayDict['jp'].joy_menu = u"メニュー表示"
    displayDict['jp'].name_hi = u"久夫"
    displayDict['jp'].name_ha = u"華子"
    displayDict['jp'].name_emi = u"笑美"
    displayDict['jp'].name_rin = u"琳"
    displayDict['jp'].name_li = u"リリー"
    displayDict['jp'].name_shi = u"静音"
    displayDict['jp'].name_mi = u"ミーシャ"
    displayDict['jp'].name_ke = u"健二"
    displayDict['jp'].name_mu = u"武藤"
    displayDict['jp'].name_nk = u"ナース"
    displayDict['jp'].name_no = u"野宮"
    displayDict['jp'].name_yu = u"優子"
    displayDict['jp'].name_sa = u"さえ"
    displayDict['jp'].name_aki = u"晃"
    displayDict['jp'].name_hh = u"秀明"
    displayDict['jp'].name_hx = u"治五郎"
    displayDict['jp'].name_emm = u"芽依子"
    displayDict['jp'].name_sk = u"店主"
    displayDict['jp'].name_mk = u"美貴"
    displayDict['jp'].name_mystery = u"？？？"
    displayDict['jp'].name_ha_ = u"紫色の髪の少女"
    displayDict['jp'].name_emi_ = u"ツインテールの少女"
    displayDict['jp'].name_rin_ = u"謎の少女"
    displayDict['jp'].name_li_ = u"ウェーブヘアの少女"
    displayDict['jp'].name_mi_ = u"笑っている少女"
    displayDict['jp'].name_ke_ = u"眼鏡をかけた生徒"
    displayDict['jp'].name_mu_ = u"背の高い男"
    displayDict['jp'].name_yu_ = u"司書"
    displayDict['jp'].name_no_ = u"白髪の男"
    displayDict['jp'].name_sa_ = u"画廊のオーナー"
    displayDict['jp'].name_aki_ = u"身なりの良い人"
    displayDict['jp'].name_nk_ = u"笑っている男"
    displayDict['jp'].name_hh_ = u"スリムな少女"
    displayDict['jp'].name_emm_ = u"三つ編みの女性"
    displayDict['jp'].name_hx_ = u"大男"
    displayDict['jp'].videos = ((u"オープニング", 'video/op_1.webm'), (u"笑美", 'video/tc_act2_emi.webm'), (u"華子", 'video/tc_act2_hanako.webm'), (u"リリー", 'video/tc_act2_lilly.webm'), (u"琳", 'video/tc_act2_rin.webm'), (u"静音", 'video/tc_act2_shizune.webm'))
    displayDict['jp'].s_scenes = ((u"プロローグ", rp_actmark, rp_actmark, ('Act 1', 'Prologue')), (u"寒空", 'NOP1', u"雪の降る寒い日、久夫の叶いかけた夢が、突然の心臓発作によって打ち砕かれる。", ('Act 1', 'Prologue')), (u"失意の久夫", 'NOP2', u"久夫は山久学園のことを聞く。そこは、高校生活の残りを送ることになる場所。", ('Act 1', 'Prologue')), (u"Act 1: 推定寿命", rp_actmark, rp_actmark, 'Act 1'), (u"入り口効果", 'A1', u"山久学園に足を踏み入れた久夫は、学級担任の武藤と会う。", 'Act 1'), (u"舞台上手へ", 'A2', u"クラスへの自己紹介、学級委員とその通訳との出会い。", 'Act 1'), (u"医療棟で", 'A3', u"ミーシャと静音に食堂へと案内された後、久夫はナースに会いに行く。", 'Act 1'), (u"空虚な部屋", 'A4', u"久夫は新しい部屋に移る途中、隣室の健二と会う。", 'Act 1'), (u"おしゃべり", 'A5', u"静音とミーシャは、久夫に学園祭が近いことを教え、昼食に誘う。", 'Act 1'), (u"リスクと報酬", 'A6', u"静音と久夫は、世界制覇を賭けたゲーム「リスク」で戦う。", 'Act 1'), (u"安らぎの紅茶", 'A7', u"図書室を探していて迷った久夫は、空き教室でリリーと出会う。", 'Act 1'), (u"図書室で二人", 'A8', u"図書室にたどり着いた久夫は華子と出会うが、彼女は怯えて逃げてしまう。", 'Act 1'), (u"奇怪千万", 'A9', u"健二が山久の隠された秘密を打ち明ける。", 'Act 1'), (u"昼ごはん進化論", 'A10', u"昼食を食べる場所を決める前に、静音とミーシャは久夫を生徒会に勧誘する。", 'Act 1'), (u"鋭い衝撃", 'A11_1', u"ミーシャと静音と一緒に昼食に行こうとした久夫は、廊下で笑美と衝突する。", 'Act 1'), (u"最悪の出会い", 'A11_2', u"華子とリリーと一緒に昼食に行こうとした久夫は、走ってきた笑美と衝突する。", 'Act 1'), (u"行きつく所へ", 'A12', u"静音とミーシャは、2人のお気に入りの茶館『上海』に久夫を連れていく。", 'Act 1'), (u"ティータイム (その1)", 'A13', u"久夫はリリーと華子と一緒に、穏やかな昼食をとる。", 'Act 1'), (u"習慣形成", 'A15', u"武藤は久夫に大事な話をしようとするが、ミーシャが割り込んで久夫に用事を頼む。", 'Act 1'), (u"遅弁", 'A16', u"資材を探していると、久夫は美術室で風変わりな少女と出会う。", 'Act 1'), (u"待ち伏せ", 'A17', u"琳を手伝ってペンキを運んでいると、久夫はナースに問い詰められる。", 'Act 1'), (u"あの緑", 'A18', u"久夫は琳が壁画を描くところを眺める。", 'Act 1'), (u"駆ける少女", 'A19', u"朝の運動に励もうとした久夫は、競技場のトラックで笑美と出会う。", 'Act 1'), (u"石鹸", 'A20', u"金を手に入れようとして、健二はシャワー室で久夫を狙う。", 'Act 1'), (u"冷戦", 'A21', u"静音とリリーは予算請求の件で火花を散らす。", 'Act 1'), (u"やる気の証", 'A22', u"静音とミーシャは、生徒会に入るよう久夫をしつこく勧誘する。", 'Act 1'), (u"事象の地平線", 'A22_2', u"静音とミーシャは、生徒会に入るよう久夫をしつこく勧誘する。", 'Act 1'), (u"さらに上を目指して", 'A23_1', u"久夫は生徒会の崇高な責務について講義を受ける。", 'Act 1'), (u"自分ができること", 'A23_2', u"静音とミーシャの魔の手から逃れた久夫は、またも琳を手伝う。", 'Act 1'), (u"ペンキ塗り", 'A24', u"華子と久夫は、リリーのクラスの屋台作りに協力する。", 'Act 1'), (u"運動", 'A25', u"早朝、久夫と笑美はふたたび一緒にトラックを走る。", 'Act 1'), (u"透明帽子", 'A26', u"健二は久夫に、人付き合いの仕方についての秘訣を伝授する。", 'Act 1'), (u"ホームグラウンドの利点", 'A26_1', u"静音とミーシャは、授業に行こうと部屋を出る久夫を拉致する。", 'Act 1'), (u"回復不可能", 'A27', False, 'Act 1'), (u"緩やかな回復", 'A27_1', u"心臓の動悸から回復し、久夫はようやく授業に出席する。", 'Act 1'), (u"回復不可能", 'A27_2', u"生徒会に連れ去られた後、久夫は授業に戻ろうと悪戦苦闘する。", 'Act 1'), (u"無料の昼食なんてない", 'A28', u"正式なメンバーとして初めて、久夫は生徒会室に行く。", 'Act 1'), (u"足と口", 'A29', u"笑美は久夫を屋上まで連れて行き、琳と一緒に昼食をとる。", 'Act 1'), (u"足元に注意", 'A30', u"久夫とリリーは買い物に行き、帰り道で混乱状態の琳と会う。", 'Act 1'), (u"支え", 'A31', u"久夫にとって初めての土曜日の授業は、武藤の説教でしめくくられる。", 'Act 1'), (u"美学", 'A32', u"笑美は放課後に暇を持て余している久夫を見つけ、またしても琳の手伝いに駆り出す。", 'Act 1'), (u"産みの苦しみ", 'A33', u"琳が壁画を描いている間に、久夫は美術教師の野宮と出会う。", 'Act 1'), (u"適度な運動", 'A34', u"笑美と久夫は、健康維持の大切さについて話し合う。", 'Act 1'), (u"ティータイム (その2)", 'A35', u"暇をつぶすため、久夫は学園の周りを散歩する。", 'Act 1'), (u"上海航路", 'A36', u"静音とミーシャと一緒に『上海』へ。お茶、ケーキ、そして勝負。", 'Act 1'), (u"お静かに", 'A37', u"学園祭の前日、華子と久夫は読書をする。", 'Act 1'), (u"あわてるな", 'A38', u"学園祭当日、目を覚ました久夫はやかましく騒ぐ健二に迎えられる。", 'Act 1'), (u"学園祭 !", 'A39', u"笑美は久夫が揚げ物を食べているところを捕まえ、罰として久夫にお供をさせる。", 'Act 1'), (u"チェックメイト", 'A42', u"リリーの屋台を手伝えなかった久夫は、学園祭の中で華子を探す。", 'Act 1'), (u"ムーブメント", 'H2', u"リリーは自分の仕事を終えて、華子と久夫を上海のお茶でもてなす。", 'Act 1'), (u"時の約束", 'A41', u"リリーの屋台で骨の折れる午前を過ごした後、久夫は彼女といっしょに華子を探す。", 'Act 1'), (u"私の頭の中の雲", 'A40', u"久夫は、琳と完成した壁画のそばで過ごす。", 'Act 1'), (u"ボール投げ", 'A44', u"約束通りに、久夫は静音とミーシャと一緒に一日を過ごす。", 'Act 1'), (u"どん底", 'A43', u"学園祭を楽しむかわりに、健二と久夫は屋上で男らしいピクニックをする。", 'Act 1'), (u"Act 2: フォーム", rp_actmark, rp_actmark, ('Act 2', 'Emi')), (u"朝練", 'E3', u"笑美とのたくさんのランニングのはじまり。", ('Act 2', 'Emi')), (u"雲と時間旅行と汝", 'E4', u"再び笑美と琳と一緒の屋上の昼食。笑美は久夫に、陸上競技会を見に行くと約束させる。", ('Act 2', 'Emi')), (u"答えの必要な質問 !", 'E5', u"笑美と久夫のたわいないおしゃべり。久夫は笑美に琳との関係をもっと詳しくたずねる。", ('Act 2', 'Emi')), (u"2度目が一番最悪", 'E6', u"2度目の朝のランニング。久夫はじたばた叫びながらトラックのまわりを半ばひきずられていく。", ('Act 2', 'Emi')), (u"一日一個のリンゴ", 'E7', u"久夫は笑美とともにナースを訪問し、以前から2人が知り合い同士だということを知る。", ('Act 2', 'Emi')), (u"陸上競技会", 'E8', u"陸上競技会の日。笑美の性格の別の側面が明らかになる。", ('Act 2', 'Emi')), (u"その薬、今すぐ飲め", 'E9', u"ナースの診察の際に久夫は胸の痛みのことを話し、説教を食らう。", ('Act 2', 'Emi')), (u"大海原の海賊稼業", 'E10', u"久夫は屋上で笑美と海賊稼業について話し合うが、岩魚子からの手紙が彼の一日を台無しにする。", ('Act 2', 'Emi')), (u"名台詞", 'E11', u"笑美、琳、久夫の3人でピクニックに出かけるが、すぐに雨によって台無しになってしまう。", ('Act 2', 'Emi')), (u"欠席調査", 'E12', u"久夫は普段通りにトラックに行くが、笑美は来ない。", ('Act 2', 'Emi')), (u"立ち寄り", 'E13', u"病気の笑美を見舞いに行ったとたん、事態は急展開する。", ('Act 2', 'Emi')), (u"事後の朝", 'E14', u"久夫は昨日の出来事を回想し、笑美を助けるためになにかしようと決意する。", ('Act 2', 'Emi')), (u"（本当の）始まり", 'E15', u"いつも通りの、しかし琳のいない、屋上でのランチタイム。", ('Act 2', 'Emi')), (u"Act 3: パースペクティブ", rp_actmark, rp_actmark, ('Act 3', 'Emi')), (u"それは……科学です", 'E16', u"武藤は久夫に、将来について短い議論をする。", ('Act 3', 'Emi')), (u"定義", 'E17', u"笑美と久夫はもう一度ピクニックを試みる、今度は母なる自然からの邪魔は入らない。", ('Act 3', 'Emi')), (u"目に見えない岩", 'E18', u"いつも通りの、朝のトラックでの走り込み……と思いきや。", ('Act 3', 'Emi')), (u"お昼ご飯と科学", 'E19', u"久夫は科学の道に進むことについて、武藤に再び相談する。", ('Act 3', 'Emi')), (u"上がって、下がって、また上がり", 'E20', u"笑美からの取り乱した電話で久夫は笑美の部屋へ急ぐ。そこで2つの驚きが待っている。", ('Act 3', 'Emi')), (u"体育倉庫", 'E21', u"笑美は久夫を陸上倉庫へと誘い込む。", ('Act 3', 'Emi')), (u"放課後の予定", 'E22', u"次の試験について笑美は久夫と真剣な話をする。", ('Act 3', 'Emi')), (u"切り離されて", 'E23', u"久夫は笑美との関係についてあれこれ考え込む。", ('Act 3', 'Emi')), (u"幻肢痛", 'E24', u"久夫が笑美に心配していることを伝えようとするが、不本意な結果に終わる。", ('Act 3', 'Emi')), (u"議論は疑念の現れ", 'E25', u"久夫は、笑美の振る舞いと笑美の家への招待に混乱する。", ('Act 3', 'Emi')), (u"お客さんは……やっぱりなし", 'E26', u"茨崎家での夕食。", ('Act 3', 'Emi')), (u"リプレイ映像", 'E27', u"ついにトラックで事情が明らかになる。", ('Act 3', 'Emi')), (u"Act 4: モーション", rp_actmark, rp_actmark, ('Act 4', 'Emi')), (u"空振り", 'E28', u"久夫は笑美に避けられているのではと怪しむ。", ('Act 4', 'Emi')), (u"セービングスロー", 'E29', u"ついに屋上で事情が明らかになる。", ('Act 4', 'Emi')), (u"過去のささやき", 'E30', u"久夫、笑美、そして笑美の母親は墓参りに出かける。", ('Act 4', 'Emi')), (u"靴下バンザイ", 'E31', u"セックス、ドラッグ、しかしロックンロールはなし。", ('Act 4', 'Emi')), (u"きれいな歯", 'E32', u"久夫が目を覚ますと、笑美が自分の隣で眠っている。", ('Act 4', 'Emi')), (u"Act 2: かくれんぼ", rp_actmark, rp_actmark, ('Act 2', 'Hanako')), (u"町へ、町へ", 'H3', u"華子と一緒にコンビニまでお買いもの。", ('Act 2', 'Hanako')), (u"茶葉", 'H4', u"華子は、リリーと一緒に昼食を食べようと久夫を誘う。", ('Act 2', 'Hanako')), (u"懺悔の生徒会室", 'H5_1', u"久夫とミーシャは華子の苦境について話し合う。", ('Act 2', 'Hanako')), (u"チェスとジェットコースター", 'H5_2', u"久夫は生徒会を放り出して、華子と一緒に本を読む。", ('Act 2', 'Hanako')), (u"朝の目覚め", 'H6', u"リリーからの放課後ティーパーティーへの誘い。", ('Act 2', 'Hanako')), (u"マッド・ハッター", 'H7', u"華子、久夫そしてリリーは一緒に集まって、リリーの部屋で紅茶を飲む。", ('Act 2', 'Hanako')), (u"小さな変化", 'H8', u"健二は借金の返済を強いられる。", ('Act 2', 'Hanako')), (u"無断欠席", 'H9', u"久夫とリリーは華子の出席状況について話し合う。", ('Act 2', 'Hanako')), (u"等価交換", 'H10', u"久夫の心臓について知ったことのお返しに、華子は久夫に自分の過去の一部を打ち明ける。", ('Act 2', 'Hanako')), (u"Act 3: キャスリング", rp_actmark, rp_actmark, ('Act 3', 'Hanako')), (u"招待", 'H11', u"リリーは久夫が紅茶部屋を片付けているのを見つけ、華子の誕生日のことを話す。", ('Act 3', 'Hanako')), (u"怪しい邂逅", 'H12', u"過去への回想と、思いがけない美貴との雑談。", ('Act 3', 'Hanako')), (u"アンティークとパイ", 'H13', u"リリーと久夫は、街でプレゼントのための買い物をする。", ('Act 3', 'Hanako')), (u"落下", 'H14', u"華子が授業中にパニック発作を起こす。", ('Act 3', 'Hanako')), (u"ゆっくりと前へ", 'H15', u"リリーは久夫と華子に悪い知らせを伝える。", ('Act 3', 'Hanako')), (u"手を伸ばして", 'H16', u"久夫は引きこもる華子に手を差し伸べる。", ('Act 3', 'Hanako')), (u"もう一年", 'H17', u"華子の誕生日を祝っていると、我らが三人衆に意外なゲストが加わる。", ('Act 3', 'Hanako')), (u"一枚の紙片", 'H18', u"久夫は初めての二日酔いを味わったあと、やっかいな手紙を受け取る。", ('Act 3', 'Hanako')), (u"ソリッドとストライプ", 'H19', u"ポケットビリヤードで遊ぶ間の、率直な話し合い。", ('Act 3', 'Hanako')), (u"終わりの始まり", 'H20', u"リリーの旅立ち。", ('Act 3', 'Hanako')), (u"Act 4: キズアト", rp_actmark, rp_actmark, ('Act 4', 'Hanako')), (u"ずる休み", 'H21', u"生徒会との昼食、そして閉じこもる華子への憂慮。", ('Act 4', 'Hanako')), (u"遠くにありて", 'H22', u"華子はさらに一日引きこもり、久夫はリリーに助言を求めて電話する。", ('Act 4', 'Hanako')), (u"つまずき", 'H23', u"久夫は華子を部屋から引き出そうとするが、驚愕する結果になる。", ('Act 4', 'Hanako')), (u"切られた花弁", 'H24', u"久夫は、華子との自分の未来の関係が、早すぎる終わりを告げたことを知る。", ('Act 4', 'Hanako')), (u"続くメロディ", 'H25', u"華子はクラスに戻り、久夫は安心する。", ('Act 4', 'Hanako')), (u"上海で勉強", 'H26', u"気が散らないように、久夫は上海で勉強しようとする。", ('Act 4', 'Hanako')), (u"彼の過去", 'H27', u"華子ともっと親しくなるために、久夫は自分の過去を華子と分かち合う。", ('Act 4', 'Hanako')), (u"シティ・ランデブー", 'H28', u"2人は街でデートする。", ('Act 4', 'Hanako')), (u"ささやきと接触", 'H29', u"久夫と華子は一夜を共に過ごす。", ('Act 4', 'Hanako')), (u"不確かな未来", 'H30', u"昨夜の出来事が久夫に重くのしかかる。", ('Act 4', 'Hanako')), (u"成熟", 'H31', u"2人の子供たちの終わり、2人の大人たちの始まり。", ('Act 4', 'Hanako')), (u"Act 2: 過去", rp_actmark, rp_actmark, ('Act 2', 'Lilly')), (u"アールグレイ", 'L1', u"昨日の疲れから回復し、久夫は華子とリリーと一緒の昼休みの最初の一日を、共に過ごす。", ('Act 2', 'Lilly')), (u"1ポンド貨", 'L2', u"健二からリリーの国籍を問われた久夫は、それよりもっと詳しく調べようとする。", ('Act 2', 'Lilly')), (u"プレゼントと存在", 'L3', u"華子のプレゼントを探している間、リリーと久夫は晃と彼女のいとこに出会う。", ('Act 2', 'Lilly')), (u"未確認飲料物体", 'L4', u"3人は華子のために誕生日パーティーを開くが、きょうだいの突然の登場に中断される。", ('Act 2', 'Lilly')), (u"あくる日", 'L5', u"目覚めた久夫とリリーは、昨夜の出来事から回復しようとする。", ('Act 2', 'Lilly')), (u"華子、『タイム』を所望する", 'L6', u"久夫とリリーは食料品を買いに出かける。", ('Act 2', 'Lilly')), (u"小さな翼", 'L7', u"屋上でみんなと分け合う昼食は残念な展開になる。", ('Act 2', 'Lilly')), (u"旅立ち", 'L8', u"リリーと晃は見送られながら、スコットランドの家族に会いに旅立つ。", ('Act 2', 'Lilly')), (u"Act 3: 現在", rp_actmark, rp_actmark, ('Act 3', 'Lilly')), (u"一日、一日", 'L9', u"久夫はぼんやりと、リリーのいない日々が過ぎるにまかせ、山久について武藤と話す。", ('Act 3', 'Lilly')), (u"小さな諍い", 'L10', u"久夫は健二と昼食をとり、気がかりなほど黙りこくっている華子にプリントを渡す。", ('Act 3', 'Lilly')), (u"不協和音", 'L11', u"完全に引きこもる華子。久夫はできる限りの助けを申し出てから、リリーに電話する。", ('Act 3', 'Lilly')), (u"遠い世界", 'L12', u"久夫は安心する一方、自分とリリーの関係について思いを巡らせる。", ('Act 3', 'Lilly')), (u"再生", 'L13', u"久夫、華子、そして秀明は、スコットランドから帰ってきた晃とリリーを出迎える。", ('Act 3', 'Lilly')), (u"北への旅", 'L14', u"3人で、北海道での休暇。", ('Act 3', 'Lilly')), (u"前奏", 'L15', u"朝の散歩から、一連の出来事が始まる。", ('Act 3', 'Lilly')), (u"クレッシェンド", 'L16', u"リリーの本当の気持ちが、果てしない黄金色の小麦畑で語られる。", ('Act 3', 'Lilly')), (u"ディミニュエンド", 'L17', u"一緒に過ごす初めての夜。", ('Act 3', 'Lilly')), (u"前途は灰色", 'L18', u"夏の別荘に閉じ込められ、リリーと久夫は自分たちの関係を受け入れざるをえない。", ('Act 3', 'Lilly')), (u"ラプソディ・イン・ブルー", 'L19', u"久夫が風呂に入りながらリリーとの関係を考えていると、何者かが一緒に入ってくる。", ('Act 3', 'Lilly')), (u"一瞬の今", 'L20', u"山久に戻る旅路の間、久夫とリリーはぼんやりと2人で話す。", ('Act 3', 'Lilly')), (u"Act 4: 未来", rp_actmark, rp_actmark, ('Act 4', 'Lilly')), (u"ワルツの前のスローステップ", 'L21', u"学校に戻ると、北海道での出来事が話題になる。", ('Act 4', 'Lilly')), (u"パジャマとスーツ", 'L22', u"日常生活に戻る。お茶会の間、晃が3人に加わる。", ('Act 4', 'Lilly')), (u"正しい手順", 'L23', u"久夫とリリーはデートの約束をする。その後、晃が顔を出す。", ('Act 4', 'Lilly')), (u"外出", 'L24', u"久夫とリリーは初めてのデートに行き、お互いの過去について知る。", ('Act 4', 'Lilly')), (u"朝のまどろみ", 'L25', u"久夫とリリーは将来の抱負について話し合う。", ('Act 4', 'Lilly')), (u"ブラックアウト", 'L26', u"3人は、近々やってくる休みについて考えにふけり、久夫はリリーの見ている視界を経験する。", ('Act 4', 'Lilly')), (u"ことの成り行き", 'L27', u"久夫は晃に呼び出され、2人はリリーのことについて話す。", ('Act 4', 'Lilly')), (u"遠い未来", 'L28', u"リリーはスコットランドの家族と一緒に暮らそうという家族の申し出を明らかにする。", ('Act 4', 'Lilly')), (u"別れ", 'L29', u"2人が日本を離れる前の晩、晃とリリーにお別れを告げる。", ('Act 4', 'Lilly')), (u"偽終止", 'L30', u"リリーの葛藤に気付いた久夫は、リリーに正面から向き合うために駆けつける。", ('Act 4', 'Lilly')), (u"涙降る空の下で", 'L31', u"病院で目覚めた久夫は、自分の人生を受け入れようとして葛藤する。", ('Act 4', 'Lilly')), (u"輝く空の下で", 'L32', u"リリーは久夫の元に戻り、2人は一緒の人生を新しく歩み始める。", ('Act 4', 'Lilly')), (u"元気に前へ !", 'L33', u"リリーと久夫は晃を見送る。", ('Act 4', 'Lilly')), (u"Act 2: すれ違い", rp_actmark, rp_actmark, ('Act 2', 'Rin')), (u"広い視野", 'R1', u"久夫は昼休みを屋上で雲を見ながら琳と過ごす。", ('Act 2', 'Rin')), (u"灰色の研究", 'R2', u"初めての美術部の活動で、琳と久夫はお互いのポートレートを描く。", ('Act 2', 'Rin')), (u"割り込み", 'R3', u"健二は久夫に「借りた」本を貸す。", ('Act 2', 'Rin')), (u"自習", 'R4', u"ミーシャと静音は授業の間、瞑想にふけりながらいたずら書きをしている久夫を捕まえる。", ('Act 2', 'Rin')), (u"久夫の笑顔", 'R5', u"琳は久夫に、彼の幸福な表情、あるいはその欠落について話す。", ('Act 2', 'Rin')), (u"好きなもの", 'R6', u"本と山久について、優子との簡単な物思い。", ('Act 2', 'Rin')), (u"対象視聴者", 'R7', u"陸上競技会の日。笑美のいろいろな面と琳のいろいろな性格が明らかになる。", ('Act 2', 'Rin')), (u"永遠の1時間", 'R8', u"野宮が部活動で芸術について議論を喚起する。", ('Act 2', 'Rin')), (u"水の中、名を持つ楓", 'R9', u"琳は久夫を森林へといざない、そこで2人は近い将来のことをじっくり考える。", ('Act 2', 'Rin')), (u"岩魚子の後悔", 'R10', u"岩魚子からの手紙が届く。", ('Act 2', 'Rin')), (u"彼女自身のイメージで", 'R11', u"久夫は琳が自分の作品の展覧会を開くのを後押しする。", ('Act 2', 'Rin')), (u"傘と論理とケーキ", 'R12', u"笑美、久夫そして琳は雨に降られて、上海に避難する。", ('Act 2', 'Rin')), (u"天国に6メートル近く", 'R13', u"琳と久夫は、笑美がいないのが明らかなので、屋上で昼食を食べ「ない」。", ('Act 2', 'Rin')), (u"優柔不断", 'R14', u"笑美は風邪を治すが、今度は琳が風邪を引いてしまう。", ('Act 2', 'Rin')), (u"シグナル・インタフェース", 'R15', u"久夫は琳を部屋に訪ねる。", ('Act 2', 'Rin')), (u"たんぽぽ", 'R16', u"丘の上で結論が下される。", ('Act 2', 'Rin')), (u"Act 3: 溝", rp_actmark, rp_actmark, ('Act 3', 'Rin')), (u"22番目の角", 'R17', u"美術部チームは琳の将来の展覧会のために画廊を下見する。", ('Act 3', 'Rin')), (u"光の薫り", 'R18', u"久夫は美術室で眠っている琳に偶然遭遇する。", ('Act 3', 'Rin')), (u"諦められないもの", 'R19', u"笑美と久夫は琳の人となりについて話し合う。", ('Act 3', 'Rin')), (u"バターン !", 'R20', u"モチベーションについての、優子の考察。", ('Act 3', 'Rin')), (u"バラ色メガネを通して", 'R21', u"野宮は芸術を職業とすることについて長々と説明する。", ('Act 3', 'Rin')), (u"世界の果て", 'R22', u"久夫は琳に告白して、振られる。本当に？", ('Act 3', 'Rin')), (u"琳の状況", 'R23', u"アトリエの奇妙でしんとした午後。", ('Act 3', 'Rin')), (u"早送り", 'R23_2', u"展覧会の準備は奇妙なパターンにはまる。", ('Act 3', 'Rin')), (u"自己破壊", 'R24', u"琳は創造性について新鮮な見方をするために、たばこを試す。", ('Act 3', 'Rin')), (u"非現実逃避", 'R25', u"久夫は琳を夜道の散歩へと連れ出す。", ('Act 3', 'Rin')), (u"限界の欠如", 'R26', u"さえと野宮は久夫に芸術家の生き様についていくつかの見識を説く。", ('Act 3', 'Rin')), (u"錯乱", 'R27', u"久夫はアトリエで自暴自棄になっている琳を驚かす。", ('Act 3', 'Rin')), (u"大嫌いなもの", 'R28', u"信じられない夜の不愉快な結末。", ('Act 3', 'Rin')), (u"怒りのかけら", 'R29', u"緊迫した2人の関係はバラバラに吹き飛ぶ。", ('Act 3', 'Rin')), (u"Act 4: 夢", rp_actmark, rp_actmark, ('Act 4', 'Rin')), (u"人々のための幻想", 'R30', u"久夫は自分の不安を野宮に伝えるが、ほとんど効果はない。", ('Act 4', 'Rin')), (u"物思いから醒まされて", 'R31', u"久夫の忍耐は終わりを迎える。", ('Act 4', 'Rin')), (u"問題のシーン", 'R32', u"展覧会のオープニングでの、琳との遭遇。", ('Act 4', 'Rin')), (u"波長", 'R35', u"久夫は、試験の最終日、無気力にダラダラと過ごす。", ('Act 4', 'Rin')), (u"青の時代", 'R36', u"雨の降る日、22nd Corner、そしてピカソの略史。", ('Act 4', 'Rin')), (u"君だけに見える世界", 'R37', u"琳と久夫は雨のあとで、別れる。", ('Act 4', 'Rin')), (u"絶望的な栄光", 'R34', u"取り乱した野宮は久夫に琳の居場所について問いただす。", ('Act 4', 'Rin')), (u"自己参照論理の問題", 'R38', u"久夫は琳が隠れているのを見つけ、野宮に謝るよう説得する。", ('Act 4', 'Rin')), (u"影を測る", 'R39', u"琳の美術教師への謝罪は、歓迎されない。", ('Act 4', 'Rin')), (u"レゾンデートル", 'R40', u"久夫は動転する琳をなぐさめる。", ('Act 4', 'Rin')), (u"息もなく、音もなく", 'R41', u"夏休みの初めの日に、琳が久夫の部屋にやってくる。", ('Act 4', 'Rin')), (u"存在の証明", 'R42', u"たんぽぽに覆われた丘の上で、すべてがあるべき場所に収まる。", ('Act 4', 'Rin')), (u"Act 2: 読む練習", rp_actmark, rp_actmark, ('Act 2', 'Shizune')), (u"伝言のやりとり", 'S8', u"静音と久夫はコミュニケーションの手段を探る。", ('Act 2', 'Shizune')), (u"手に向かって話しかけて", 'S9', u"久夫は新しい言語を勉強し始め、個人指導者が登場する。", ('Act 2', 'Shizune')), (u"伝言ゲーム", 'S10', u"健二は久夫に無理矢理頼み事をするが、久夫はさまざまな困難に見舞われる。", ('Act 2', 'Shizune')), (u"上級ゲーム理論", 'S11', u"もうリスクゲームでは静音の飢えを満たせない。さらに新しい敵までもが登場する。", ('Act 2', 'Shizune')), (u"じゃん・けん・パン", 'S12', u"一切れのパンが突然強烈な興味の対象になり、けだるげな午後が劇的なものに変わる。", ('Act 2', 'Shizune')), (u"インターフェイス", 'S13', u"静音と久夫はつながりを見出す。", ('Act 2', 'Shizune')), (u"即時対応", 'S14', u"久夫はリリーと静音の仲裁をするはめになるが、幸い最後には丸く収まる。", ('Act 2', 'Shizune')), (u"過去不完全型", 'S15', u"上海でくつろいでいる間、生徒会は過去の年月を回想する。", ('Act 2', 'Shizune')), (u"星々が抱き合うとき", 'S16', u"ついに七夕の日が来た！", ('Act 2', 'Shizune')), (u"Act 3: 器用な手つき", rp_actmark, rp_actmark, ('Act 3', 'Shizune')), (u"フォースフィードバック", 'S17', u"久夫は静音が実家に戻るのを知って、ついて行くことに成功する。", ('Act 3', 'Shizune')), (u"国際連合", 'S18', u"静音の実家への旅、彼女の弟との出会い、そして突然の魚釣り競争。", ('Act 3', 'Shizune')), (u"使用と言及の区別", 'S19', u"秀明は久夫をもてなそうとするが、あまりうまくいかない。", ('Act 3', 'Shizune')), (u"家族陰謀", 'S20', u"我らが三人衆は静音の父に会い、すぐさま早々に引き上げる。", ('Act 3', 'Shizune')), (u"パングラム", 'S21', u"秀明の手話を学びたいという要望は、治五郎との怒鳴りあいという予想外の事態に発展する。", ('Act 3', 'Shizune')), (u"もっとそばに", 'S22', u"静音と久夫は、はじめて、ひとつになる。", ('Act 3', 'Shizune')), (u"対決", 'S23', u"治五郎が生徒会を過小評価するので、久夫はその挑戦を受けて立つ。", ('Act 3', 'Shizune')), (u"錨", 'S24', u"山久に戻る。岩魚子からの手紙と、ガールフレンドの詳細について健二の長話。", ('Act 3', 'Shizune')), (u"ロードマップ", 'S25', u"生徒会は自分たちの後任について心配し、久夫はなぜかミーシャにパフェをおごるはめになる。", ('Act 3', 'Shizune')), (u"鋭角三角関係", 'S26', u"静音との午後の仕事で、久夫は静音とミーシャの仲がぎくしゃくしていることを見て取る。", ('Act 3', 'Shizune')), (u"十進分類法", 'S27', u"優子は久夫に図書室の番を頼む。健二の到着で、その試みは半分失敗、半分成功する。", ('Act 3', 'Shizune')), (u"もつれる舌", 'S28', u"ミーシャは久夫を部屋に訪ねる。そして物事は予想しない方向へ向かう。", ('Act 3', 'Shizune')), (u"脇を見て", 'S29_1', u"久夫は落ち込んだミーシャと屋上で出会う。そしてミーシャと静音を無理矢理引き合わせる。", ('Act 3', 'Shizune')), (u"正面を見て", 'S29_2', u"久夫は落ち込んだミーシャと屋上で出会う。静音は2人に合流し、みんなを仕事にひき戻す。", ('Act 3', 'Shizune')), (u"Act 4: もう一人の私へ", rp_actmark, rp_actmark, ('Act 4', 'Shizune')), (u"大戦略", 'S30', u"静音は久夫に自身の目標と失敗を告白する。", ('Act 4', 'Shizune')), (u"わずかなずれ", 'S31', u"ミーシャを元気づけようという失敗した試みは、久夫と静音の即興デートに変化する。", ('Act 4', 'Shizune')), (u"侵略", 'S32', u"治五郎と秀明が突然静音を訪れるが、どこか不愉快なものに終わる。", ('Act 4', 'Shizune')), (u"パフェ", 'S33', u"久夫と静音はミーシャのあとをつける。久夫はとうとうミーシャを追い詰め、きちんと話をする。", ('Act 4', 'Shizune')), (u"現在形", 'S38', u"久夫は昼食の時、リリーに偶然出会い、2人は静音について話す。", ('Act 4', 'Shizune')), (u"らせん", 'S39', u"その場しのぎの言い逃れ、はぐらかし、そして健二の夜襲。", ('Act 4', 'Shizune')), (u"終焉", 'S40', u"沈黙の学園で静音と早朝の会話。", ('Act 4', 'Shizune')), (u"頂点", 'S34', u"健二と静音が久夫の部屋で邂逅する。奇跡的に、何も爆発しない。", ('Act 4', 'Shizune')), (u"引き継ぎ", 'S35', u"「課外活動」に従事する前に、在任中の生徒会が後任を鍛え上げる。", ('Act 4', 'Shizune')), (u"隠密行動", 'S36', u"ミーシャが示した決意は、静音がより広い物事に目を向けるのに拍車をかける。", ('Act 4', 'Shizune')), (u"無限", 'S37', u"卒業を間近に控え、我らが3人は友情を新しくする。", ('Act 4', 'Shizune')))
    displayDict['jp'].creditstring = u"{image=ui/flourish_left.png} {b}ライター{/b} {image=ui/flourish_right.png}\nAnonymous22\nAura\ncpl_crud\nSuriko\nTheHivemind\n\n{image=ui/flourish_left.png} {b}編集{/b} {image=ui/flourish_right.png}\nKagami\nLosstarot\nSilentcook\n\n{image=ui/flourish_left.png} {b}音楽{/b} {image=ui/flourish_right.png}\nBlue123\nNicolArmarfi\n\n{image=ui/flourish_left.png} {b}美術{/b} {image=ui/flourish_right.png}\ngebyy-terar\nKamifish\nmoekki\npimmy\nraemz\nRaide\n\n{image=ui/flourish_left.png} {b}美術補{/b} {image=ui/flourish_right.png}\nclimatic\nDoomfest\nyujovi\n\n{image=ui/flourish_left.png} {b}アニメーション{/b} {image=ui/flourish_right.png}\nMike Inel\n\n{image=ui/flourish_left.png} {b}ディレクション{/b} {image=ui/flourish_right.png}\ndelta\nRaide\nyujovi\n\n{image=ui/flourish_left.png} {b}技術{/b} {image=ui/flourish_right.png}\ndelta\n\n{image=ui/flourish_left.png} {b}翻訳{/b} {image=ui/flourish_right.png}\na-park\nAce Toyoda\nan tuck\nBlackmountain Big\ncolul\nDaice\nEEE boy\ngaksh\nhardwired Okano\nhatayan\nhir\nKoumoto\nKyoDong Ryo\nlaich\nMirai\nNishimori Reo\nNagi\nnaita\nRushhh\ntomoya\nTextAdventureFreak\nTK\nzig5z7\n秋茄子トマト\nゴン太\n\n{image=ui/flourish_left.png} {b}プロデューサー{/b} {image=ui/flourish_right.png}\ncpl_crud\nSuriko\n\n\n{image=ui/flourish_center.png}\n\n\n{image=ui/flourish_left.png} {b}謝辞{/b} {image=ui/flourish_right.png}\nAmbi07\nabscess\nAnonymous\nCeliest\nContinualNaba\nDark_Mercury\nDuaneMoody\nFink\nfrumplstlskn\nIsmuth\nJapesland\nJuno\nkekekeke\nkonflikti\nMagaran\nMirage_GSM\nOverCoat\nPeorth\nPetaru\nsilentkyon\nskim\nstirfriedweasel\nSyureria\nTcDohl\ntottori\nVCR\n\n{image=ui/flourish_left.png} {b}スペシャルサンクス{/b} {image=ui/flourish_right.png}\nhir\nPyTom\nRAITA"
    displayDict['jp'].drugs_wordlist = [u"ジソピラミド", u"ワルファリン", u"ジルチアゼム", u"フェロジピン", u"プロプラノロール", u"ペンブトロール", u"カルテオロール", u"プロカインアミド", u"ヘパリン", u"フェニトイン", u"ベラパミル", u"キニジン", u"フレカイニド", u"5mg/日", u"400mg/日", u"15ml/日", u"100mg/日", u"10ml/48時間", u"10ml/日", u"200mg/12時間", u"50mg/12時間", u"500mg/48時間", u"125mg/12時間", u"25ml/日", u"悪夢", u"集中力低下", u"徐脈", u"鬱病", u"不眠症", u"勃起不全", u"視覚異常", u"心臓麻痺", u"悪心", u"眩暈", u"幻覚", u"気管支痙攣", u"呼吸困難", u"疲労", u"低血圧", u"心臓ブロック", u"四肢冷感", u"下痢", u"心停止", u"心室細動", u"失調症", u"喘息"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
