DELETE FROM Games;
DELETE FROM Rating;
DELETE FROM Publishers;
DELETE FROM Developers;

SET SERVEROUTPUT ON
DECLARE
    rows NUMBER(2) := 3;
    TYPE GameName IS VARRAY(3) OF VARCHAR2(100 CHAR);
    TYPE Rating IS VARRAY(3) OF VARCHAR2(50 CHAR);
    TYPE ReleaseDate IS VARRAY(3) OF VARCHAR2(50 CHAR);
    TYPE Publisher IS VARRAY(3) OF VARCHAR2(50 CHAR);
    TYPE Developer IS VARRAY(3) OF VARCHAR2(50 CHAR);
   
    name_arr GameName := GameName('Hollow Knight', 'Undertale', 'Fran Bow');
    rating_arr Rating := Rating('EC', 'E10+', 'E');
    release_date_arr ReleaseDate := ReleaseDate('Feb 24.2017', 'Sep 15.2015', 'Aug 27.2015');
    publisher_arr Publisher := Publisher('Team Cherry', 'tobyfox', 'Killmonday Games HB');
    developer_arr Developer := Developer('Team Cherry', 'tobyfox', 'Killmonday Games HB');
    
BEGIN
    FOR i in 1..rows LOOP
        INSERT INTO Rating(rating)
        VALUES (rating_arr(i));
    
        INSERT INTO Publishers(publisher)
        VALUES (publisher_arr(i));
    
        INSERT INTO Developers(developer)
        VALUES (developer_arr(i));    
    
        INSERT INTO Games(gname, rating, publisher, developer, release_date)
        VALUES (name_arr(i), rating_arr(i), publisher_arr(i), developer_arr(i), release_date_arr(i));
    END LOOP;
END;
/