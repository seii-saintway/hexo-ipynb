const path = require('path')
const exec = require('co-exec')
const co = require('co')

const PY_SCRIPT = path.join(__dirname, 'convert.py')

hexo.extend.tag.register('asset_ipynb', function (args) {
  return co(function *() {
    const ipynbFile = path.join(hexo.source_dir, args[0])

    let html = yield exec(`/usr/bin/python ${PY_SCRIPT} ${ipynbFile}`, {
      maxBuffer: 5 * 1024 * 1024,
      env: {
        PYTHONIOENCODING: 'utf8'
      }
    })

    return html
  })

}, {
  async: true,
  ends: false
})
