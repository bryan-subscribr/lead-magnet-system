from PIL import Image
F='frames/'; O='../img/'
C=[
('hin_108','trends_what_people_look_for',(390,380,1600,900)),
('hin_143','trends_new_videos_inspire',(400,440,1600,1075)),
('hin_40','audience_channels_watch_dark',(800,180,1900,1080)),
('hin_46','audience_what_they_watch_dark',(800,330,1600,1080)),
('hin_331','reach_content_suggesting',(0,330,740,920)),
('hin_386','reach_search_terms_dark',(560,250,1560,780)),
('hin_350','advanced_traffic_source_dark',(500,150,1920,1080)),
('jer_14','analytics_tabs_light',(300,90,1900,600)),
('jer_20','trends_get_ideas',(320,200,1920,800)),
('jer_29','trends_topic_page',(380,200,1900,1075)),
('jer_41','trends_saved_hearts',(380,200,1900,1080)),
('tea_23.5','trends_tea_2026',(160,60,1760,920)),
('tea_18.5','audience_watch_behavior_tea',(160,60,1760,920)),
('tea_31','reach_card_tea',(160,60,1760,920)),
('tea_48.5','reach_thumbnail_impressions',(380,120,1540,1080)),
('tea_8.5','analytics_overview_tea',(160,60,1760,920)),
('think_734','video_viewers_also_watch',(300,370,1530,1050)),
('think_855','advanced_mode_button',(700,100,1760,560)),
('think_878','advanced_mode_table',(0,90,1530,1080)),
('think_926','advanced_content_type_filter',(100,0,1530,1080)),
('insp_10','inspiration_content_tab',(0,0,1920,1080)),
('insp_22','inspiration_brainstorm_box',(620,140,1300,900)),
('insp_42','inspiration_idea_page',(420,120,1500,960)),
('insp_66','inspiration_titles',(380,100,1520,980)),
('mou_42','insights_new_home',(130,70,1790,1010)),
('mou_48','insights_research_new',(130,70,1790,1010)),
('mou_108','draft_feedback',(130,70,1790,1010)),
('ab_20','ab_thumbnail_section',(180,100,1740,980)),
('ab_50','ab_dialog',(440,90,1460,990)),
('ab_80','ab_view_test_report',(300,0,1920,1000)),
('ab_116','ab_test_report',(440,100,1480,1060)),
('and_25','research_old_explore',(80,100,1880,730)),
('and_85','research_old_content_gap_tooltip',(280,300,1200,1080)),
('and_105','research_old_content_gap_labels',(250,250,1190,1080)),
('and_165','research_old_content_gap_labels2',(250,250,1190,1080)),
('nate_53','reach_suggested_overview_dark',(340,40,1740,1040)),
('nate_113','reach_suggested_table_dark',(0,0,1920,1080)),
('nate_41','analytics_tabs_2024_research',(0,0,1920,700)),
('hin_309','reach_video_cards_dark',(0,100,1200,1000)),
]
for src,name,box in C:
    im=Image.open(F+src+'.jpg').convert('RGB').crop(box)
    if im.width>1600: im=im.resize((1600,int(im.height*1600/im.width)))
    im.save(O+name+'.jpg',quality=88)
print(len(C))
