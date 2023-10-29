import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    probability_distribution = dict()
    corpus_length = len(corpus)

    # Page has no outgoing link, We set equal distribution of all corpus page
    if len(corpus[page]) < 1:
        for key in corpus:
            probability_distribution[key] = 1 / corpus_length
    # Page have outgoing links, So we calclutate distribution
    else:
        adding_factor = damping_factor / len(corpus[page])
        random_factor = (1 - damping_factor) / corpus_length

        for key in corpus:
            probability_distribution[key] = random_factor
            if key in corpus[page]:
                probability_distribution[key] += adding_factor

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = dict()
    # Set pages distribution zero
    for key in corpus:
        page_rank[key] = 0

    # First time set sample as random value
    sample = random.choice(list(corpus.keys()))
    for i in range(n):
        distribution = transition_model(corpus, sample, damping_factor)
        key, value = zip(*distribution.items())
        sample = random.choices(key, weights=value, k=1)[0]
        page_rank[sample] += 1

    for key in page_rank:
        page_rank[key] /= n

    return page_rank
    
    

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    old_rank = dict()
    new_rank = dict()
    corpus_length = len(corpus)

    # Set eqaul distribution to every page rank and add in old_rank dictonary 
    for page in corpus:
        old_rank[page] = 1 / corpus_length

    # Formula to calculate the distribution
    difference = 1
    while difference > 0.001:
        for page in corpus:
            rank = 0
            for linking_page in corpus:
                # Check if page links to our page
                if page in corpus[linking_page]:
                    rank += (old_rank[linking_page] / len(corpus[linking_page]))
                # If page has no links, means it as having one link for every other page
                if len(corpus[linking_page]) == 0:
                    rank += (old_rank[linking_page]) / corpus_length
            rank *= damping_factor
            rank += (1 - damping_factor) / corpus_length

            new_rank[page] = rank

        # Calculating difference between old and new distribution value
        difference = max([abs(new_rank[x] - old_rank[x]) for x in old_rank])
        
        # Set condition if difference is less tahn from given value the we can't update old_dict value and return
        # as it is. 
        if difference > 0.001:
            old_rank = new_rank.copy()

    return old_rank

if __name__ == "__main__":
    main()