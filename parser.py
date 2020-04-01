#!/usr/bin/python
from os.path import join, abspath
from urllib.parse import urljoin

import simplejson as json
from bs4 import BeautifulSoup

NOVA_VERSIONS = ("3.0", "2.0", "1.0")
NOVA_DOCS_URL = "https://nova.laravel.com/docs/{version}"


def parse():
    entries = []

    for version in NOVA_VERSIONS:
        with open(abspath(join("docs", version, "index.html")), "r") as index_html:
            index_soup = BeautifulSoup(index_html, "lxml")

            sidebar_links = index_soup.find("ul", class_="sidebar-links")
            if sidebar_links:
                for sidebar_link in sidebar_links.find_all("a", class_="sidebar-link"):
                    href = sidebar_link.get("href")

                    if href.startswith("/docs/{}/installation.html".format(version)):
                        continue
                    if href.endswith("/"):
                        href += "index.html"

                    title = " ".join(sidebar_link.get_text().split()).strip()

                    if "#" in href:
                        file, id = href.split("#")
                    else:
                        file, id = href, None

                    file = abspath(file[1:])
                    if not file.endswith(".html"):
                        file += "/index.html"

                    try:
                        with open(file) as html:
                            try:
                                topic_soup = BeautifulSoup(html, "lxml")
                                topic = topic_soup.find(id=id)
                                parent = topic.parent

                                entry_data = {
                                    "version": float(version),
                                    "id": id,
                                    "title": title,
                                    "permalink": urljoin(
                                        NOVA_DOCS_URL.format(version=version), href
                                    ),
                                    "categories": [],
                                    "content": "",
                                }

                                if id:
                                    h1 = topic_soup.find("h1")
                                    if h1:
                                        category = " ".join(
                                            topic_soup.find("h1").get_text().split()
                                        ).strip()
                                        if category:
                                            if category.startswith("# "):
                                                category = category[2:]
                                            entry_data["categories"].append(category)

                                # set the content
                                while True:
                                    content = " ".join(
                                        topic.find_next("p").get_text().split()
                                    ).strip()
                                    if content:
                                        entry_data["content"] = content
                                        break

                                entries.append(entry_data)
                            except Exception:
                                print(href)
                                print(parent.name)
                                raise
                    except Exception:
                        print(file[1:])
                        raise

    if entries:
        with open(abspath("data.json"), "w") as fh:
            json.dump(entries, fh, indent=4)


if __name__ == "__main__":
    parse()
