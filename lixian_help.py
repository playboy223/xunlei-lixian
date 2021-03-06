
basic_usage = '''python lixian_cli.py <command> [<args>]

Basic commands
 help       try this help...
 login      login Xunlei cloud
 download   download tasks from Xunlei cloud
 list       list tasks on Xunlei cloud
 add        add tasks to Xunlei cloud
 delete     delete tasks from Xunlei cloud
 pause      pause tasks on Xunlei cloud
 restart    restart tasks on Xunlei cloud
 config     save configuration so you don't have to repeat it
 info       print user id, internal user id, and gdriveid
 logout     logout from Xunlei cloud
'''

def usage():
	return basic_usage + '''
Use 'python lixian_cli.py help' for details.
Use 'python lixian_cli.py help <command>' for more information on a specific command.
Check https://github.com/iambus/xunlei-lixian for detailed (and Chinese) doc.'''

help_help = '''Get helps:
  python lixian_cli.py help help
  python lixian_cli.py help examples
  python lixian_cli.py help readme
  python lixian_cli.py help <command>'''

help = help_help

welcome = '''Python script for Xunlei cloud.

Basic usage:
''' + basic_usage + '\n' + help_help

def examples():
	return '''python lixian_cli.py login "Your Xunlei account" "Your password"
python lixian_cli.py login "Your password"
python lixian_cli.py login

python lixian_cli.py config username "Your Xunlei account"
python lixian_cli.py config password "Your password"

python lixian_cli.py list
python lixian_cli.py list --completed
python lixian_cli.py list --completed --name --original-url --download-url --no-status --no-id
python lixian_cli.py list id1 id2
python lixian_cli.py list zip rar
python lixian_cli.py list --search zip rar

python lixian_cli.py download task-id
python lixian_cli.py download ed2k-url
python lixian_cli.py download --tool wget ed2k-url
python lixian_cli.py download --tool asyn ed2k-url
python lixian_cli.py download ed2k-url --output "file to save"
python lixian_cli.py download id1 id2 id3
python lixian_cli.py download url1 url2 url3
python lixian_cli.py download --input download-urls-file
python lixian_cli.py download --input download-urls-file --delete
python lixian_cli.py download --input download-urls-file --ouput-dir root-dir-to-save-files
python lixian_cli.py download bt://torrent-info-hash
python lixian_cli.py download --torrent 1.torrent
python lixian_cli.py download --torrent torrent-info-hash
python lixian_cli.py download --torrent http://xxx/xxx.torrent

python lixian_cli.py add url
python lixian_cli.py add --torrent 1.torrent
python lixian_cli.py add --torrent torrent-info-hash
python lixian_cli.py add --torrent http://xxx/xxx.torrent

python lixian_cli.py delete task-id
python lixian_cli.py delete url
python lixian_cli.py delete file-name-on-cloud-to-delete

python lixian_cli.py pause id

python lixian_cli.py restart id

python lixian_cli.py logout

Please check https://github.com/iambus/xunlei-lixian for detailed (and Chinese) doc.
'''

def readme():
	import sys
	import os.path
	doc = os.path.join(sys.path[0], 'README.md')
	with open(doc) as txt:
		return txt.read().decode('utf-8')


login    = '''python lixian_cli.py login <username> <password>

login Xunlei cloud

Examples:
 python lixian_cli.py login "Your Xunlei account" "Your password"
 python lixian_cli.py login "Your password"
 python lixian_cli.py login
'''

download = '''python lixian_cli.py download [options] [id|url]...

download tasks from Xunlei cloud

Options:
 --input=[file]    -i            Download URLs found in file.
 --output=[file]   -o            Download task to file.
 --output-dir=[dir]              Download task to dir.
 --tool=[wget|asyn|aria2|curl]   Choose download tool.
                                 Default: wget
 --continue        -c            Continue downloading a partially downloaded file.
                                 Default: false.
 --overwrite                     Overwrite partially downloaded file.
                                 Default: false.
 --delete                        Delete task from Xunlei cloud after download is finished.
                                 Default: false.
 --torrent                       Treat all arguments as torrent files (e.g. local torrent file, torrent http url, torrent info hash)
                                 Default: false.
 --all                           Download all tasks. This option will be ignored if specific download URLs or task ids can be found. 
                                 Default: false.
 --search                        Treat all arguments as keywords of cloud tasks
                                 Default: false.
 --hash                          When this option is false (--no-hash), never do full hash, but a minimal hash will be performed (supposed to be very fast).
                                 Default: true.
 --mini-hash                     If the target file already exists, and the file size is complete, do a minimal hash (instead of full hash, which would be much more expensive). This is useful when you are resuming a batch download, in this case the previously downloaded and verified files won't be re-verified.
                                 Default: false.

Examples:
 python lixian_cli.py download task-id
 python lixian_cli.py download ed2k-url
 python lixian_cli.py download --tool wget ed2k-url
 python lixian_cli.py download --tool asyn ed2k-url
 python lixian_cli.py download ed2k-url --output "file to save"
 python lixian_cli.py download id1 id2 id3
 python lixian_cli.py download url1 url2 url3
 python lixian_cli.py download --input download-urls-file
 python lixian_cli.py download --input download-urls-file --delete
 python lixian_cli.py download --input download-urls-file --ouput-dir root-dir-to-save-files
 python lixian_cli.py download bt://torrent-info-hash
 python lixian_cli.py download --torrent 1.torrent
 python lixian_cli.py download --torrent torrent-info-hash
 python lixian_cli.py download --torrent http://xxx/xxx.torrent
 python lixian_cli.py download bt-task-id/file-id
 python lixian_cli.py download --all
'''

list     = '''python lixian_cli.py list

list tasks on Xunlei cloud

Options:
 --complete           Print only complete tasks. Default: no
 --[no]-id            Print task id. Default: yes
 --[no]-name          Print task name. Default: yes
 --[no]-status        Print task status. Default: yes
 --[no]-size          Print task size. Default: no
 --[no]-progress      Print task progress (in percent). Default: no
 --[no]-speed         Print task speed. Default: no
 --[no]-original-url  Print the original URL. Default: no
 --[no]-download-url  Print the download URL used to download from Xunlei cloud. Default: no

Examples:
 python lixian_cli.py list
 python lixian_cli.py list id
 python lixian_cli.py list bt-task-id/
 python lixian_cli.py list --completed
 python lixian_cli.py list --completed --name --original-url --download-url --no-status --no-id
 python lixian_cli.py list id1 id2
 python lixian_cli.py list zip rar
 python lixian_cli.py list --search zip rar
'''

add      = '''python lixian_cli.py add [options] url...

add tasks to Xunlei cloud

Options:
 --input=[file]                  Download URLs found in file.
 --torrent                       Treat all arguments as torrent files (e.g. local torrent file, torrent http url, torrent info hash)
                                 Default: false.

Examples:
 python lixian_cli.py add url
 python lixian_cli.py add --torrent 1.torrent
 python lixian_cli.py add --torrent torrent-info-hash
 python lixian_cli.py add --torrent http://xxx/xxx.torrent
'''

delete   = '''python lixian_cli.py delete [options] [id|url|filename|keyword]...

delete tasks from Xunlei cloud

Options:
 -i     prompt before delete
 --all  delete all tasks if there are multiple matches

Examples:
 python lixian_cli.py delete task-id
 python lixian_cli.py delete url
 python lixian_cli.py delete file-name-on-cloud-to-delete
'''

pause    = '''python lixian_cli.py pause [options] [id|url|filename|keyword]...

pause tasks on Xunlei cloud

Options:
 -i     prompt before pausing tasks
 --all  pause all tasks if there are multiple matches
'''

restart  = '''python lixian_cli.py restart [id|url|filename|keyword]...

restart tasks on Xunlei cloud

Options:
 -i     prompt before restart
 --all  restart all tasks if there are multiple matches
'''

config   = '''python lixian_cli.py config key [value]

save configuration so you don't have to repeat it

Examples:
 python lixian_cli.py config username "your xunlei id"
 python lixian_cli.py config password "your xunlei password"
 python lixian_cli.py config continue
'''

info     = '''python lixian_cli.py info

print user id, internal user id, and gdriveid'''

logout   = '''python lixian_cli.py logout

logout from Xunlei cloud
'''


