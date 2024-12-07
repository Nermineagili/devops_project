import { screen } from '@testing-library/dom';
import '@testing-library/jest-dom';

const htmlContent = `
  <h1>Upload an Audio File</h1>
  <form id="uploadForm" enctype="multipart/form-data" data-testid="uploadForm">
    <input type="file" id="fileInput" accept="audio/*" required data-testid="fileInput">
    <button type="submit">Classify</button>
  </form>
  <p id="result" data-testid="result"></p>
`;

beforeEach(() => {
  document.body.innerHTML = htmlContent;
});

describe('Audio File Upload Form', () => {
  it('renders the form elements correctly', () => {
    // Check if the form, input, and result elements are rendered
    const form = screen.getByTestId('uploadForm');
    const fileInput = screen.getByTestId('fileInput');
    const resultParagraph = screen.getByTestId('result');

    expect(form).toBeInTheDocument();
    expect(fileInput).toBeInTheDocument();
    expect(resultParagraph).toBeInTheDocument();
  });
});
