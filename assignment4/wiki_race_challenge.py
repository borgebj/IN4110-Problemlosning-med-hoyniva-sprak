from typing import List  # isort:skip

from requesting_urls import get_html
from filter_urls import find_articles
import time

from collections import deque
from typing import Callable


def average_time(function: Callable, *args, calls: int = 1) -> (List[str], float):
    times = []
    paths = []

    for i in range(calls):
        t0 = time.perf_counter()
        paths.append(function(*args))
        t1 = time.perf_counter()
        times.append(t1-t0)

    return min(paths, key=len), sum(times) / len(times)


def countdown(sec):
    time.sleep(1)
    while sec > 0:
        print(f'[{sec}]', end=" ")
        sec -= 1
        time.sleep(1)


def BFS_shortest_path(start: str, goal: str) -> List[str]:
    """Breadth-first search algorithm, for traversing a graph

    Traverses a link and all its sub-links to find a path
    between first url and second url

    Arguments:
        start (string) : string containing URL to start on
        goal (string) : string containing URL to end up on
    Returns:
        new_path (list) : a list containing the path from start to goal in URL-form
    """
    # visited = [[start]]
    queue = [[start]]

    visited = [[start]]
    # queue = deque([start])

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            for article in find_articles(get_html(node), all_lan=False):
                new_path = list(path)
                new_path.append(article)
                queue.append(new_path)

                if article == goal:
                    return new_path

            visited.append(node)
    return []


def find_path(start: str, finish: str, calls: int) -> List[str]:
    """Find the shortest path from `start` to `finish`

    Uses Breadth-first search algorithm to search through all articles of each url,
    to then first the shortest path to the end-article

    Arguments:
      start (str): wikipedia article URL to start from
      finish (str): wikipedia article URL to stop at
      calls (int): how many calls for the timing function
    Returns:
      urls (list[str]):
        List of URLs representing the path from `start` to `finish`.
        The first item should be `start`.
        The last item should be `finish`.
        All items of the list should be URLs for wikipedia articles.
        Each article should have a direct link to the next article in the list.
    """
    # race countdown + info
    print("Warning : A sound will play when path is found!")
    time.sleep(3)
    print("\nStarting wiki-race in ...")
    countdown(3)
    print("\n\n- Search has begun -")

    # starts timing
    t0 = time.perf_counter()
    time_start = time.strftime("%H:%M:%S", time.localtime())

    path, avg = average_time(BFS_shortest_path, start, finish, calls=calls)

    time_end = time.strftime("%H:%M:%S", time.localtime())
    t1 = time.perf_counter()
    # ends timing

    # can take time, so makes a sound when finished
    import winsound
    winsound.Beep(1000, 500)

    # inform of output
    print("\n"+("-"*100))
    print(f'Shortest path: {path}')
    print(f'Total time: {t1-t0:.2f}s on {calls} runs with {avg:.2f}s average')
    print(f'Time at start: {time_start}')
    print(f'Time at end: {time_end}')
    print("-"*100)

    assert path[0] == start
    assert path[-1] == finish
    return path


if __name__ == "__main__":
    # default
    # start = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    # finish = "https://en.wikipedia.org/wiki/Peace"

    # shorter
    # start = 'https://en.wikipedia.org/wiki/J._K._Rowling'
    # finish = 'https://en.wikipedia.org/wiki/World_War_II'

    # shortest
    start = "https://en.wikipedia.org/wiki/Pentacora"
    finish = "https://en.wikipedia.org/wiki/Adolf_Hitler"
    calls = 1

    find_path(start, finish, calls)

    # note: time can vary, since urls can contain lots of links + articles is a set
    # 2 samples from example links above:

    # pc 1 average 393s
    # 340, 746, 731, 344, 600, 112, 556, 155, 143, 446, 132, 412
    # fastest: 112s

    # pc 2 average: 453s
    # 556, 603, 139, 710, 282, 599, 177, 544, 380, 403, 702, 344
    # fastest: 139s

    # tests done on random links:

    # start = "https://en.wikipedia.org/wiki/Paul_Grof"
    # finish = "https://en.wikipedia.org/wiki/Kopust"
    # time taken: 3270s / 54m
    # path length: 5 links
    # paul_grof -> main_page -> druidry_(modern) -> hassidic -> kopust

    # start = "https://en.wikipedia.org/wiki/Pentacora"
    # finish = "https://en.wikipedia.org/wiki/Adolf_Hitler"
    # time taken: 18s
    # path length: 4 links
    # pentacora -> isbn_(identifier) -> book_burning -> adolf_hitler

    # 6.39, 10.44, 5.66, 16.33, 49.85, 9.04, 58.20, 28.25, 32.86, 5.87