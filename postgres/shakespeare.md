ответы на задание Task Shakespeare
# 1
select plaintext from wordform limit 10;
# 2
select plaintext from wordform where plaintext ilike 'a%';
# 3
select title from work where genretype = 'p';
# 4
select avg(totalparagraphs) from work where genretype = 't';
# 5
select title from work where totalwords > (select avg(totalwords) from work);
# 6
select character.charname, speechcount, work.title from character join character_work on character_work.charid = character.charid join work on character_work.workid = work.workid;
# 7
SELECT ROUND(avg(speechcount)), work.title FROM character JOIN character_work ON character.charid = character_work.charid JOIN work ON character_work.workid = work.workid WHERE work.title = 'Romeo and Juliet' GROUP BY work.title; 
# 8
select section, sum(wordcount) from paragraph group by section
# 9
select charname, speechcount from character where speechcount between 15 and 30;
# 10
select title, year from work where year between 1601 and 1700;
# 11
select longtitle from work where longtitle like '%the%';
# 12
select distinct section from paragraph;
# 13
select chapter.chapterid,  chapter.description, title from work join chapter on chapter.workid = work.workid;
# 14
select paragraphnum, character.charname, character.speechcount from paragraph join character on paragraph.charid = character.charid;
# 15
select paragraphnum, work.title, work.year from paragraph join work on work.workid = paragraph.workid;


