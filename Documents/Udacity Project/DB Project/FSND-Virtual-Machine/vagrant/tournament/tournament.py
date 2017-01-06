#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database.
    DELETE FROM matches;"""
    conn = connect()
    # cursor to execute statements
    db_cursor = conn.cursor()
    # query statement
    query = "DELETE FROM matches;"
    # execute the query
    db_cursor.execute(query)
    # write to the database
    conn.commit()
    # close the connection
    conn.close()


def deletePlayers():
    """Remove all the player records from the database.
    DELETE FROM players; """
    conn = connect()
    # cursor to execute the statement
    db_cursor = conn.cursor()
    # query statement
    query = "DELETE FROM players;"
    # execute the query
    db_cursor.execute(query)
    # write to the database
    conn.commit()
    # close the connection
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    """ select COUNT(id) as num from players; """
    conn = connect()
    # cursor to execute statement
    db_cursor = conn.cursor()
    # query statement
    query = "SELECT COUNT(id) AS num FROM players;"
    # execute the query
    db_cursor.execute(query)
    # write to the database
    results = db_cursor.fetchone()
    conn.commit()
    # close the connection
    conn.close()
    #return 0 if there are no values to countPlayers
    if results:
        return results[0]
    else:
        return '0'


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    # cursor to execute statement
    db_cursor = conn.cursor()
    # query statement
    query = "INSERT INTO players(name) VALUES(%s);"
    #make name a tuple to be used in the execute method
    argument = tuple([name])
    # execute the commands
    db_cursor.execute(query, argument)
    # commit to the database
    conn.commit()
    # cloes the connection
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    # cursor to execute command
    db_cursor = conn.cursor()
    # query statement
    query = """
                SELECT * from v_standings;
                """
    # execute the commands
    db_cursor.execute(query)
    standing = db_cursor.fetchall()
    # close the connection
    conn.close()
    return standing


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      insert into matches VALUES ('%s', '%s') (winner, loser)
    """
    conn = connect()
    #cursor
    db_cursor = conn.cursor()
    query = "INSERT INTO matches (winner, loser) values (%s, %s);"
    db_cursor.execute(query, (int(winner,), int(loser)))
    #commit to the database
    conn.commit()
    #close the connection
    conn.close()
    """
        returns a list of two players for a match
    """
def pairings(list, size = 2):
    return [list[i:i + size] for i in range(0, len(list), size)]

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    paired_pool = pairings(standings, 2)
    matched_pairs = list()


    for paired in paired_pool:
        pairing = list()
        for player in paired:
            pairing.append(player[0])
            pairing.append(player[1])
        matched_pairs.append(pairing)

    return matched_pairs
