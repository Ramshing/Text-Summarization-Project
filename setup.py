import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()


__version__="0.0.0"

Repo_Name="Text-Summarization-Project"
Author_User_Name="Ramshing"
src_repo="TextSummarizer"
Author_Email="ramkdinesh@gmail.com"



setuptools.setup(
    name=src_repo,
    version=__version__,
    author=Author_User_Name,
    author_email=Author_Email,
    description="python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_User_Name}/{Repo_Name}",
    project_urls={
        "Bug Tracker":f"https://github.com/{Author_User_Name}/{Repo_Name}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)