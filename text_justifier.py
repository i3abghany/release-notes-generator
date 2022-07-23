import re

from urlextract import URLExtract


class TextJustifier:

    def __init__(self, line_break, url_pattern):
        self.line_break = line_break
        self.url_pattern = url_pattern

    def wrap(self, text, width=50):
        text = text.replace('\r\n', ' \n ').strip()
        lines = ['']
        effective_lens = [0]
        words = list(map(lambda w: w.replace('\u200b', ''), re.sub(r'(\S)\n(\S)', r'\1 \n \2', text).split(' ')))
        url_extractor = URLExtract()
        for i, word in enumerate(words):
            is_url = url_extractor.has_urls(word)
            word_effective_len = len(word)
            if word == '\n' and effective_lens[-1] != width:
                lines.append('')
                effective_lens.append(0)
                continue

            if word.find('```') != -1:
                effective_lens[-1] = width  # Fill the line to enforce a break.

            if is_url and len(word) > width - effective_lens[-1]:
                word_effective_len = len("link")
                word = self.url_pattern.format("link", word)
            if effective_lens[-1] + word_effective_len < width or (is_url and (effective_lens[-1] + word_effective_len < width)):
                lines[-1] += (' ' + word.strip())
                if is_url and not (effective_lens[-1] + word_effective_len < width):
                    effective_lens[-1] += word_effective_len
                else:
                    effective_lens[-1] += len((' ' + word.strip()))
                if word.find('\n') != -1:
                    effective_lens[-1] = width
                    continue
            elif word_effective_len <= width:
                lines.append('')
                lines[-1] += word
                effective_lens.append(word_effective_len)
                if word.find('\n') != -1:
                    effective_lens[-1] = width
                    continue
            else:
                splits = self._hard_wrap_line(word, width)
                for split in splits:
                    if effective_lens[-1] + len(split) < width:
                        lines[-1] += split
                        effective_lens[-1] += len(split)
                    else:
                        lines.append('')
                        lines[-1] += split
                        effective_lens.append(len(split))

        return self.line_break.join(lines)

    @staticmethod
    def _hard_wrap_line(text, width):
        lines = []
        i = 0
        while i < len(text):
            lines.append(text[i:min(len(text), i + width)])
            i += width
        return lines
