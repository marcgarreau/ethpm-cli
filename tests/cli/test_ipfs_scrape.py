import pexpect


def test_ipfs_scrape(tmp_path):
    ipfs_dir = tmp_path / "ipfs"
    ipfs_dir.mkdir()
    child = pexpect.spawn(f"ethpm scrape --ipfs-dir {ipfs_dir} --start-block 1")
    child.expect("EthPM CLI v0.1.0a0\r\n")
    child.expect("\r\n")
    child.expect("Scraping from block 1.\r\n")
    child.expect("Blocks 1-5001 scraped. 0 VersionRelease events found.\r\n")